from dependency_injector import containers, providers

from .cases import ScansCases
from .repos import DefaultScansRepo


class Container(containers.DeclarativeContainer):
    storage = providers.DependenciesContainer()

    scans_repo = providers.Singleton(DefaultScansRepo, storage.db_session)
    scans_cases = providers.Singleton(ScansCases, scans_repo)
