from pydantic import BaseModel


class InstitutionTypeEntity(BaseModel):
    type: str
