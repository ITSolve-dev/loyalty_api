from core import BaseRepo, IRetrieveRepo, IDeleteRepo, ICreateRepo

from ..models import Profile
from ..schemas import AddProfileRolesSchema, RetrieveProfileSchema


class IProfileRepo(BaseRepo, IDeleteRepo, IRetrieveRepo, ICreateRepo):
    table = Profile

    async def add_roles(self, id: int, data: AddProfileRolesSchema) -> RetrieveProfileSchema:
        raise NotImplemented
