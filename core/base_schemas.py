from typing import TypeVar, Generic, List, Optional
from pydantic import RootModel, BaseModel, ConfigDict
from datetime import datetime

T = TypeVar("T")

"""
Example:

Orm Table Model
class Model:
    name: str
    age: int

ModelSchema: Describe fields of business model data. As db model, but except id

OrmModelSchema: Model with id field and can validate from model instance. Default Schema

CreateModelSchema: Data need for creation business model instance in database. Without id. Maybe same as ModelSchema

DetailedModelSchema: Detailed model - with relations(deep)

LightModelSchema: Light model - only ids in relations

ListModelSchema(Generic[T], RootModel[List[T]]): Generic List of schemas

UpdateModelSchema: Data need for update. Maybe same as CreateModelSchema or ModelSchema, but all optional

DeleteModelSchema: (Optional)Data need for deleting. 90% only id need for deleting, except of cascade tables
"""


class OrmSchema(BaseModel):
    """
    Orm schema for instance from database table.
    Schema with id field
    """

    id: int
    model_config = ConfigDict(from_attributes=True)


class DateTimeMixinSchema(BaseModel):
    """
    Mixin schema add datetime fields
    """

    created_at: datetime
    updated_at: Optional[datetime] = None


class ListModelSchema(RootModel[List[T]], Generic[T]):
    pass
