from core import BaseRepo, ICreateRepo

from ..models import User


class IUserRepo(BaseRepo, ICreateRepo):
    table: User = User
