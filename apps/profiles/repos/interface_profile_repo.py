from core import BaseRepo, IRetrieveRepo, IDeleteRepo, ICreateRepo

from ..models import Profile


class IProfileRepo(BaseRepo, IDeleteRepo, IRetrieveRepo, ICreateRepo):
    table = Profile

