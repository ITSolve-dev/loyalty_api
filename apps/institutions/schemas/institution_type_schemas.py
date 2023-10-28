from core import OrmSchema

from ..entities import InstitutionTypeEntity


class InstitutionTypeSchema(InstitutionTypeEntity, OrmSchema):
    pass


class CreateInstitutionTypeSchema(InstitutionTypeEntity):
    pass


class RetrieveInstitutionTypeSchema(InstitutionTypeSchema):
    pass
