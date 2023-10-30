from core import BaseCases

from ..repos import DefaultLoyaltyTicketsRepo
from ..schemas import *


class LoyaltyTicketsCases(BaseCases[DefaultLoyaltyTicketsRepo]):
    async def create(self, data: CreateLoyaltyTicketSchema) -> RetrieveLoyaltyTicketSchema:
        return await self.repo.create(data=data)

    async def retrieve(self, id: int) -> RetrieveLoyaltyTicketSchema:
        return await self.repo.retrieve(id=id)
