from typing import Optional
from sqlalchemy import exc

from ..schemas import CreateUserSchema, RetrieveUserSchema
from .interface_user_repo import IUserRepo
from ..exceptions import UsersAlreadyExistsException


class DefaultUserRepo(IUserRepo):
    async def create(self, data: CreateUserSchema) -> Optional[RetrieveUserSchema]:
        try:
            user = await self.default_create_instance(data=data)
        except exc.IntegrityError:
            raise UsersAlreadyExistsException
        else:
            return RetrieveUserSchema.model_validate(user)
