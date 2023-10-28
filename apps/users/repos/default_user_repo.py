from typing import Optional

import sqlalchemy as sa
from loguru import logger
from db.orm import start_session

from ..schemas import CreateUserSchema, RetrieveUserSchema
from .interface_user_repo import IUserRepo


class DefaultUserRepo(IUserRepo):
    async def create(self, data: CreateUserSchema) -> Optional[RetrieveUserSchema]:
        user = await self.default_create_instance(data=data)
        return RetrieveUserSchema.model_validate(user)
