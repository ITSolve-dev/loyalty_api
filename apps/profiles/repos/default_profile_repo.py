import sqlalchemy as sa
from typing import Optional

from dependency_injector.wiring import Provide, inject
from sqlalchemy.orm import joinedload

from db.orm import start_session
from apps.users.repos import DefaultRoleRepo
from apps.users.schemas import CreateRoleSchema

from ..models import Profile
from ..schemas import CreateProfileSchema, RetrieveProfileSchema, AddProfileRolesSchema
from .interface_profile_repo import IProfileRepo
from ..exceptions import ProfileNotFoundException, ProfileRolesExistException


class DefaultProfileRepo(IProfileRepo):
    @inject
    async def create(
        self, data: CreateProfileSchema, role_repo: DefaultRoleRepo = Provide["user_app.role_repo"]
    ) -> Optional[RetrieveProfileSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.insert(self.table)
                .values(**data.model_dump(exclude={"role"}))
                .returning(self.table.id)
            )
            profile_id: int = await session.scalar(query)

            await role_repo.create(CreateRoleSchema(type=data.role, profile_id=profile_id))

            query = (
                sa.select(self.table)
                .where(self.table.id == profile_id)
                # .options(joinedload(self.table.user))
                .options(joinedload(self.table.roles))
            )
            profile: Profile = await session.scalar(query)
            return RetrieveProfileSchema.model_validate(profile)

    async def add_roles(
        self,
        id: int,
        data: AddProfileRolesSchema,
        role_repo: DefaultRoleRepo = Provide["user_app.role_repo"],
    ) -> RetrieveProfileSchema:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(self.table.id == id)
                .options(joinedload(self.table.roles))
            )
            profile: Profile = await session.scalar(query)
            income_role_types = set(data.roles)
            exist_role_types = map(lambda role: role.type, profile.roles)
            need_to_add_types = list(set(income_role_types) - set(exist_role_types))

            if not need_to_add_types:
                raise ProfileRolesExistException

            for role_type in need_to_add_types:
                await role_repo.create(CreateRoleSchema(type=role_type, profile_id=profile.id))

        return await self.retrieve(id=id)

    async def delete(self, id: int) -> Optional[RetrieveProfileSchema]:
        pass

    async def retrieve(self, id: int) -> Optional[RetrieveProfileSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(self.table.id == id)
                # .options(joinedload(self.table.user))
                .options(joinedload(self.table.roles))
            )
            profile: Profile = await session.scalar(query)
            if not profile:
                raise ProfileNotFoundException
            return RetrieveProfileSchema.model_validate(profile)
