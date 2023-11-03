from typing import Sequence

from pydantic import BaseModel

from core import OrmSchema, DateTimeMixinSchema, ListModelSchema

from ..entities import InstitutionEntity
from .institution_type_schemas import RetrieveInstitutionTypeSchema
from .member_schemas import RetrieveMemberSchema


class InstitutionSchema(OrmSchema, InstitutionEntity):
    pass


class CreateInstitutionSchema(InstitutionEntity):
    pass


class RetrieveInstitutionSchema(InstitutionSchema, DateTimeMixinSchema):
    type: RetrieveInstitutionTypeSchema
    members: list[RetrieveMemberSchema]


class AddUsersInstitutionSchema(BaseModel):
    user_ids: Sequence[int]


class ListInstitutionSchema(ListModelSchema[RetrieveInstitutionSchema]):
    pass


class LoyaltyTicketToInstitutionSchema(BaseModel):
    amount: int
    activated: bool


class RetrieveInstitutionToCustomerSchema(InstitutionSchema):
    type: RetrieveInstitutionTypeSchema
    customer_tickets: list[LoyaltyTicketToInstitutionSchema]


class ListInstitutionsToCustomerSchema(ListModelSchema[RetrieveInstitutionToCustomerSchema]):
    pass
