from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import InstitutionType


class IInstitutionTypeRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = InstitutionType
