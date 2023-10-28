from dependency_injector import containers, providers

from db.containers import StorageContainer

from .cases import ProfileCases
from .repos import DefaultProfileRepo


class Container(containers.DeclarativeContainer):
    storage: StorageContainer = providers.DependenciesContainer()

    profile_repo = providers.Singleton(DefaultProfileRepo, storage.db_session)
    profile_cases = providers.Singleton(ProfileCases, profile_repo)
