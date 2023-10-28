from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class OrmSchema(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)


class DateTimeMixinSchema(BaseModel):
    created_at: datetime
    updated_at: Optional[datetime] = None
