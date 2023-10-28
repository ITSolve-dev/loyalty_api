from typing import Optional

from core import BaseCases, AppException

from ..schemas import CreateUserSchema, RetrieveUserSchema
from ..repos import DefaultUserRepo


class UserCases(BaseCases[DefaultUserRepo]):
    async def create_user(self, data: CreateUserSchema) -> RetrieveUserSchema:
        user = await self.repo.create(data=data)
        if not user:
            raise AppException(error='error')
        return user
