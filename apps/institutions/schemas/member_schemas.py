from typing import Optional
from pydantic import BaseModel

from core import OrmSchema, DateTimeMixinSchema
from apps.profiles.schemas import RetrieveProfileSchema

from ..entities import MemberEntity


class MemberSchema(MemberEntity, OrmSchema):
    pass


class CreateMemberSchema(BaseModel):
    active: Optional[bool] = True
    profile_id: int
    institution_id: int


class RetrieveMemberSchema(MemberSchema, DateTimeMixinSchema):
    profile: RetrieveProfileSchema
    institution_id: int
