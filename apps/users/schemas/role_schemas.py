from pydantic import BaseModel

from core import OrmSchema

from ..entities import RoleType


class RoleSchema(OrmSchema):
    type: RoleType


class CreateRoleSchema(BaseModel):
    type: RoleType
    profile_id: int


class RetrieveRoleSchema(RoleSchema, OrmSchema):
    pass


class DeleteRoleSchema(OrmSchema):
    pass
