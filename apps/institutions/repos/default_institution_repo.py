import sqlalchemy as sa
from typing import Optional, Sequence

from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import joinedload

from db.orm import start_session
from apps.users.models import User
from apps.users.entities import RoleType
from apps.profiles.schemas import CreateProfileSchema
from apps.profiles.repos import DefaultProfileRepo
from apps.scans.models import LoyaltyTicket

from ..schemas import *
from ..exceptions import *
from .interface_institution_repo import IInstitutionRepo
from .default_institution_type_repo import DefaultInstitutionTypeRepo
from .default_members_repo import DefaultMemberRepo


class DefaultInstitutionRepo(IInstitutionRepo):
    @inject
    async def create(
        self,
        data: CreateInstitutionSchema,
        institution_type_repo: DefaultInstitutionTypeRepo = Provide[
            "institutions_app.institution_type_repo"
        ],
    ) -> Optional[RetrieveInstitutionSchema]:
        async with start_session(self.db_session) as session:
            institution_type = await institution_type_repo.create(
                CreateInstitutionTypeSchema(**data.type.model_dump())
            )
            query = (
                sa.insert(self.table)
                .values(**data.model_dump(exclude={"type"}), type_id=institution_type.id)
                .returning(self.table.id)
            )
            institution_id: int = await session.scalar(query)

        return await self.retrieve(id=institution_id)

    async def retrieve(self, id: int) -> Optional[RetrieveInstitutionSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(self.table.id == id)
                .options(joinedload(self.table.type))
                .options(joinedload(self.table.members))
            )
            institution = await session.scalar(query)

            if not institution:
                raise InstitutionNotFoundException
            return RetrieveInstitutionSchema.model_validate(institution)

    @inject
    async def add_users(
        self,
        id: int,
        user_ids: Sequence[int],
        profile_repo: DefaultProfileRepo = Provide["profiles_app.profile_repo"],
        members_repo: DefaultMemberRepo = Provide["institutions_app.members_repo"],
    ) -> RetrieveInstitutionSchema:
        await self.retrieve(id=id)
        async with start_session(self.db_session) as session:
            query = sa.select(User.id).where(User.id.in_(user_ids))
            db_user_ids: list[int] = (await session.scalars(query)).all()
            not_exist_ids = list(set(user_ids) - set(db_user_ids))
            if not_exist_ids:
                raise InstitutionAddUsersNotExistsException(ctx={"not_exist_ids": not_exist_ids})

            for user_id in db_user_ids:
                profile = await profile_repo.create(
                    CreateProfileSchema(user_id=user_id, role=RoleType.EMPLOYEE)
                )

                await members_repo.create(
                    CreateMemberSchema(institution_id=id, profile_id=profile.id)
                )
        return await self.retrieve(id=id)

    async def get_by_customer_profile_id(self, id: int) -> ListInstitutionSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(LoyaltyTicket.profile_id == id)
                .options(joinedload(self.table.customer_tickets))
            )
            institutions = list(
                filter(
                    lambda institution: id
                    in list(map(lambda ticket: ticket.id, institution.customer_tickets)),
                    (await session.scalars(query)).unique().all(),
                )
            )
        return ListInstitutionSchema.model_validate(institutions)
