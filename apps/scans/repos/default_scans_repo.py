import sqlalchemy as sa
from typing import Optional
from sqlalchemy.orm import joinedload
from dependency_injector.wiring import Provide, inject

from db.orm import start_session
from apps.profiles.repos import DefaultProfileRepo
from apps.users.entities import RoleType

from ..models import Scan, LoyaltyTicket
from ..schemas import *
from ..exceptions import *
from .interface_loyalty_tickets_repo import ILoyaltyTicketsRepo
from .interface_scans_repo import IScansRepo


class DefaultScansRepo(IScansRepo):
    async def __get_loyalty_ticket_created(self, id: int) -> Optional[LoyaltyTicket]:
        async with start_session(self.db_session) as session:
            query = sa.select(LoyaltyTicket).where(LoyaltyTicket.id == id)
            ticket = await session.scalar(query)
        return ticket

    @inject
    async def create(
        self,
        data: CreateScanSchema,
        profile_repo: DefaultProfileRepo = Provide["profiles_app.profile_repo"],
        loyalty_ticket_repo: ILoyaltyTicketsRepo = Provide["scans_app.loyalty_tickets_repo"],
    ) -> Optional[RetrieveScanSchema]:
        async with start_session(self.db_session) as session:
            if data.object_profile_id == data.subject_profile_id:
                raise ScansPermissionException(
                    ctx={
                        "error": f"Object id == Subject id - {data.object_profile_id} = {data.subject_profile_id}"
                    }
                )
            subject_profile = await profile_repo.get_profile_instance(id=data.subject_profile_id)
            object_profile = await profile_repo.get_profile_instance(id=data.object_profile_id)
            if (
                subject_profile.role in (RoleType.EMPLOYEE, RoleType.DEVELOPER)
                and object_profile.role != RoleType.EMPLOYEE
                and subject_profile.active_institution
            ):
                loyalty_ticket = object_profile.get_active_ticket_by_institution_id(
                    subject_profile.active_institution.id
                )
                if not loyalty_ticket:
                    loyalty_ticket = await loyalty_ticket_repo.create(
                        CreateLoyaltyTicketSchema(
                            profile_id=object_profile.id,
                            institution_id=subject_profile.active_institution.id,
                        )
                    )
                query = (
                    sa.insert(self.table)
                    .values(**data.model_dump(), loyalty_ticket_id=loyalty_ticket.id)
                    .returning(self.table.id)
                )
                scan_id: int = await session.scalar(query)
            else:
                raise ScansPermissionException(
                    ctx=dict(
                        object=f"Object role must not be {RoleType.EMPLOYEE.value}",
                        subject=f"Subject role must be {RoleType.EMPLOYEE.value}",
                    )
                )
        return await self.retrieve(id=scan_id)

    async def retrieve(self, id: int) -> Optional[RetrieveScanSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(
                    self.table,
                )
                .where(self.table.id == id)
                .options(joinedload(self.table.object_profile))
                .options(joinedload(self.table.subject_profile))
                .options(joinedload(self.table.institution))
            )
            scan: Scan = await session.scalar(query)
        return RetrieveScanSchema.model_validate(scan)

    async def get_scans_profile(self, profile_id: int) -> ListScanSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(
                    self.table,
                )
                .where(self.table.subject_profile_id == profile_id)
                .options(joinedload(self.table.object_profile))
                .options(joinedload(self.table.subject_profile))
                .options(joinedload(self.table.institution))
            )
            scans = (await session.scalars(query)).unique().all()

            query = sa.select(sa.func.sum(self.table.amount)).where(
                self.table.subject_profile_id == profile_id
            )
            sum_scans_amount = await session.scalar(query)
            return ListScanSchema.model_validate(
                dict(
                    scans=scans,
                    amount=len(scans),
                    sum_scans_amount=sum_scans_amount if sum_scans_amount else 0,
                )
            )

    async def get_scanned_profile(self, profile_id: int) -> ListScanSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(
                    self.table,
                )
                .where(self.table.object_profile_id == profile_id)
                .options(joinedload(self.table.object_profile))
                .options(joinedload(self.table.subject_profile))
                .options(joinedload(self.table.institution))
            )
            scans = (await session.scalars(query)).unique().all()
            query = sa.select(sa.func.sum(self.table.amount)).where(
                self.table.subject_profile_id == profile_id
            )
            sum_scans_amount = await session.scalar(query)
            return ListScanSchema.model_validate(
                dict(
                    scans=scans,
                    amount=len(scans),
                    sum_scans_amount=sum_scans_amount if sum_scans_amount else 0,
                )
            )
