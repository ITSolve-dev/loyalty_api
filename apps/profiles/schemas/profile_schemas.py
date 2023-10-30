from typing import Optional
from pydantic import BaseModel, Field

from core import OrmSchema, DateTimeMixinSchema

from apps.users.schemas import RetrieveUserSchema
from apps.users.entities import RoleType

from ..entities import ProfileEntity


class ProfileSchema(ProfileEntity, OrmSchema):
    pass


class CreateProfileSchema(BaseModel):
    user_id: int
    role: Optional[RoleType] = Field(default=RoleType.CUSTOMER)


class UpdateProfileSchema(ProfileEntity):
    pass


class RetrieveProfileSchema(ProfileSchema, DateTimeMixinSchema):
    user: RetrieveUserSchema


class RetrieveUserWithProfileSchema(RetrieveUserSchema):
    profile: RetrieveProfileSchema


class DeleteProfileSchema(OrmSchema):
    pass
