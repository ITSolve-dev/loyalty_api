from datetime import datetime
from typing import Optional, Sequence

from pydantic import BaseModel

from core import OrmSchema
from apps.profiles.schemas import ProfileSchema, RetrieveProfileSchema


class ScanSchema(OrmSchema):
    object_profile: ProfileSchema
    subject_profile: ProfileSchema
    created_at: datetime


class CreateScanSchema(BaseModel):
    object_profile_id: int
    subject_profile_id: int
    amount: Optional[int] = 1


class RetrieveScanSchema(ScanSchema):
    object_profile: RetrieveProfileSchema
    subject_profile: RetrieveProfileSchema


class ListScanSchema(BaseModel):
    scans: Sequence[RetrieveScanSchema]
    amount: int
    sum_scans_amount: int
