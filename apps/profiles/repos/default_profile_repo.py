import sqlalchemy as sa
from typing import Optional, List

from pydantic import TypeAdapter

from db.orm import start_session

from ..models import Profile
from ..schemas import CreateProfileSchema, RetrieveProfileSchema
from .interface_profile_repo import IProfileRepo
from ..exceptions import ProfileNotFoundException


class DefaultProfileRepo(IProfileRepo):

    async def create(
        self, data: CreateProfileSchema
    ) -> Optional[RetrieveProfileSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.insert(self.table)
                .values(**data.model_dump())
                .returning(self.table.id)
            )
            profile_id: int = await session.scalar(query)

            query = (
                sa.select(self.table)
                .where(self.table.id == profile_id)
            )
            profile: Profile = await session.scalar(query)
            return RetrieveProfileSchema.model_validate(profile)

    async def delete(self, id: int) -> Optional[RetrieveProfileSchema]:
        pass

    async def retrieve(self, id: int) -> Optional[RetrieveProfileSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table)
                .where(self.table.id == id)
            )
            profile: Profile = await session.scalar(query)
            if not profile:
                raise ProfileNotFoundException
            return RetrieveProfileSchema.model_validate(profile)

    async def get_profiles_by_telegram_id(self, telegram_id: int) -> List[RetrieveProfileSchema]:
        async with start_session(self.db_session) as session:
            query = (
                sa.select(self.table).where(self.table.user.has(telegram_id=telegram_id))
            )

            profiles = (await session.scalars(query)).unique().all()
            ta = TypeAdapter(List[RetrieveProfileSchema])
            return ta.validate_python(profiles)
