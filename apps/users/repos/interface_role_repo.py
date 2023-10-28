from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import Role


class IRoleRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = Role
