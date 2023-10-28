from pydantic import BaseModel

from apps.profiles.entities import ProfileEntity


class MemberEntity(BaseModel):
    active: bool
    profile: ProfileEntity
