from pydantic import BaseModel

from .institution_type_entity import InstitutionTypeEntity


class InstitutionEntity(BaseModel):
    name: str
    type: InstitutionTypeEntity
