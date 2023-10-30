from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel

from core import OrmSchema
from apps.profiles.schemas import ProfileSchema, RetrieveProfileSchema
from apps.institutions.schemas import RetrieveInstitutionSchema


class ScanSchema(OrmSchema):
    amount: int
    object_profile: ProfileSchema
    subject_profile: ProfileSchema
    created_at: datetime


class CreateScanSchema(BaseModel):
    object_profile_id: int
    subject_profile_id: int
    loyalty_ticket_id: int
    amount: Optional[int] = 1


class CreateScanWithoutLoyaltySchema(BaseModel):
    object_profile_id: int
    subject_profile_id: int
    amount: Optional[int] = 1


class RetrieveScanSchema(ScanSchema):
    object_profile: RetrieveProfileSchema
    subject_profile: RetrieveProfileSchema
    institution: RetrieveInstitutionSchema


class LightScanSchema(OrmSchema):
    amount: int
    object_profile_id: int
    subject_profile_id: int
    loyalty_ticket_id: int
    created_at: datetime


class ListScanSchema(BaseModel):
    scans: Sequence[RetrieveScanSchema]
    sum_scans_amount: Optional[int] = 0
