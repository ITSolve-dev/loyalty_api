from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import LoyaltyTicket


class ILoyaltyTicketsRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = LoyaltyTicket
