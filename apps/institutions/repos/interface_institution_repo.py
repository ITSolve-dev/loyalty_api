from typing import Sequence

from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import Institution
from ..schemas import *


class IInstitutionRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = Institution

    async def add_users(self, id: int, user_ids: Sequence[int]) -> RetrieveInstitutionSchema:
        raise NotImplemented

    async def get_by_customer_profile_id(self, id: int) -> ListInstitutionSchema:
        raise NotImplemented
