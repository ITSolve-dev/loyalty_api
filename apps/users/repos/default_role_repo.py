from typing import Optional

from db.orm import start_session

from ..schemas import CreateRoleSchema, RetrieveRoleSchema
from .interface_role_repo import IRoleRepo


class DefaultRoleRepo(IRoleRepo):
    async def create(self, data: CreateRoleSchema) -> Optional[RetrieveRoleSchema]:
        role = await self.default_create_instance(data=data)
        return RetrieveRoleSchema.model_validate(role)

    async def retrieve(self, id: int) -> Optional[RetrieveRoleSchema]:
        role = await self.default_retrieve_instance(id=id)
        return RetrieveRoleSchema.model_validate(role)
