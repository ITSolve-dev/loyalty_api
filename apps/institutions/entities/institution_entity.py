from pydantic import BaseModel

from .institution_type_entity import InstitutionTypeEntity
from .member_entity import MemberEntity


class InstitutionEntity(BaseModel):
    name: str
    type: InstitutionTypeEntity
    members: list[MemberEntity]
