import sqlalchemy as sa
from typing import Optional
from sqlalchemy.orm import joinedload
from dependency_injector.wiring import Provide, inject

from db.orm import start_session
from apps.profiles.repos import DefaultProfileRepo
from apps.profiles.schemas import RetrieveProfileSchema
from apps.users.entities import RoleType

from ..models import Scan
from ..schemas import *
from .interface_scans_repo import IScansRepo


class DefaultScansRepo(IScansRepo):
    @inject
    async def create(self, data: CreateScanSchema, profile_repo: DefaultProfileRepo = Provide['profiles_app.profile_repo']) -> Optional[RetrieveScanSchema]:
        async with start_session(self.db_session) as session:
            subject_profile = await profile_repo.retrieve(id=data.subject_profile_id)
            object_profile = await profile_repo.retrieve(id=data.object_profile_id)
            # if RoleType.EMPLOYEE in subject_profile.roles:
            query = sa.insert(self.table).values(**data.model_dump()).returning(self.table.id)
            scan_id: int = await session.scalar(query)
        return await self.retrieve(id=scan_id)

    async def retrieve(self, id: int) -> Optional[RetrieveScanSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(self.table.id == id)
                .options(joinedload(self.table.object_profile))
                .options(joinedload(self.table.subject_profile))
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
            )
            scans = (await session.scalars(query)).unique().all()
            query = sa.select(sa.func.sum(self.table.amount)).where(
                self.table.subject_profile_id == profile_id
            )
            sum_scans_amount = await session.scalar(query)
            return ListScanSchema.model_validate(
                dict(scans=scans, amount=len(scans), sum_scans_amount=sum_scans_amount)
            )
