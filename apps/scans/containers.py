from dependency_injector import containers, providers

from .cases import ScansCases, LoyaltyTicketsCases
from .repos import DefaultScansRepo, DefaultLoyaltyTicketsRepo


class Container(containers.DeclarativeContainer):
    storage = providers.DependenciesContainer()

    scans_repo = providers.Singleton(DefaultScansRepo, storage.db_session)
    scans_cases = providers.Singleton(ScansCases, scans_repo)

    loyalty_tickets_repo = providers.Singleton(DefaultLoyaltyTicketsRepo, storage.db_session)
    loyalty_tickets_cases = providers.Singleton(LoyaltyTicketsCases, loyalty_tickets_repo)
