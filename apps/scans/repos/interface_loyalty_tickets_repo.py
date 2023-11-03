from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import LoyaltyTicket
from ..schemas import RetrieveLoyaltyTicketSchema


class ILoyaltyTicketsRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = LoyaltyTicket

    async def activate_ticket(self, id: int) -> RetrieveLoyaltyTicketSchema:
        raise NotImplemented
