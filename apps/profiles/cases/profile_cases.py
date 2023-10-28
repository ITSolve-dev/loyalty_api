from core import BaseCases

from ..repos import DefaultProfileRepo
from ..schemas import *


class ProfileCases(BaseCases[DefaultProfileRepo]):
    async def create(self, data: CreateProfileSchema) -> RetrieveProfileSchema:
        return await self.repo.create(data=data)

    async def retrieve(self, profile_id: int) -> RetrieveProfileSchema:
        return await self.repo.retrieve(id=profile_id)

    async def add_roles(self, profile_id: int, data: AddProfileRolesSchema) -> RetrieveProfileSchema:
        return await self.repo.add_roles(data=data, id=profile_id)
