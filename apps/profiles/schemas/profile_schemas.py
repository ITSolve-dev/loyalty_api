from typing import Iterable
from pydantic import BaseModel

from core import OrmSchema, DateTimeMixinSchema

from apps.users.schemas import RetrieveUserSchema, RetrieveRoleSchema
from apps.users.entities import RoleType

from ..entities import ProfileEntity


class ProfileSchema(ProfileEntity, OrmSchema):
    pass


class CreateProfileSchema(BaseModel):
    user_id: int
    role: RoleType


class AddProfileRolesSchema(BaseModel):
    roles: Iterable[RoleType]


class UpdateProfileSchema(ProfileEntity):
    pass


class RetrieveProfileSchema(ProfileSchema, DateTimeMixinSchema):
    user: RetrieveUserSchema
    roles: Iterable[RetrieveRoleSchema]


class DeleteProfileSchema(OrmSchema):
    pass
