from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import ProfileToInstitution


class IMembersRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = ProfileToInstitution
