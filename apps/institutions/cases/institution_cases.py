from typing import Sequence

from core import BaseCases, handle_validation_exc

from ..schemas import *
from ..repos import DefaultInstitutionRepo
from ..exceptions import InstitutionValidationException


class InstitutionCases(BaseCases[DefaultInstitutionRepo]):
    @handle_validation_exc(InstitutionValidationException)
    async def create(self, data: CreateInstitutionSchema) -> RetrieveInstitutionSchema:
        return await self.repo.create(data=data)

    @handle_validation_exc(InstitutionValidationException)
    async def retrieve(self, id: int) -> RetrieveInstitutionSchema:
        return await self.repo.retrieve(id=id)

    async def add_users(self, id: int, user_ids: Sequence[int]) -> RetrieveInstitutionSchema:
        return await self.repo.add_users(id=id, user_ids=user_ids)
