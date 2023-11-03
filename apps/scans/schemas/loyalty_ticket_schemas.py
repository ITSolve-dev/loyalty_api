from typing import Sequence, Optional, List
from pydantic import Field, BaseModel, RootModel

from core import OrmSchema, DateTimeMixinSchema

from apps.profiles.schemas import ProfileSchema, RetrieveProfileSchema
from apps.institutions.schemas import InstitutionSchema, RetrieveInstitutionSchema
from .scans_schemas import (
    ScanSchema,
    LightScanSchema,
    CreateScanWithoutLoyaltySchema,
)


class LoyaltyTicketSchema(OrmSchema, DateTimeMixinSchema):
    profile: ProfileSchema
    institution: InstitutionSchema
    activated: Optional[bool] = Field(default=False)
    scans: Sequence[ScanSchema]


class CreateLoyaltyTicketSchema(BaseModel):
    profile_id: int
    institution_id: int
    activated: Optional[bool] = Field(default=False)
    scans: Optional[Sequence[CreateScanWithoutLoyaltySchema]] = []


class RetrieveLoyaltyTicketSchema(OrmSchema):
    profile: RetrieveProfileSchema
    institution: RetrieveInstitutionSchema
    activated: bool
    scans: List[LightScanSchema]


class ListLoyaltyTicketSchema(RootModel[List[RetrieveLoyaltyTicketSchema]]):
    pass
