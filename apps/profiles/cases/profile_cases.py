from core import BaseCases

from ..repos import DefaultProfileRepo
from ..schemas import *


class ProfileCases(BaseCases[DefaultProfileRepo]):
    async def create(self, data: CreateProfileSchema) -> RetrieveProfileSchema:
        return await self.repo.create(data=data)

    async def retrieve(self, profile_id: int) -> RetrieveProfileSchema:
        return await self.repo.retrieve(id=profile_id)

    async def get_profiles_by_telegram_id(self, telegram_id: int) -> list[RetrieveProfileSchema]:
        return await self.repo.get_profiles_by_telegram_id(telegram_id=telegram_id)
