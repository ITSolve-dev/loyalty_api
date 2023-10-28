from dependency_injector import containers, providers

from db import StorageContainer

from .repos import DefaultUserRepo, DefaultRoleRepo
from .cases import UserCases


class Container(containers.DeclarativeContainer):
    storage: StorageContainer = providers.DependenciesContainer()

    user_repo = providers.Singleton(DefaultUserRepo, storage.db_session)
    user_cases = providers.Singleton(UserCases, user_repo)

    role_repo = providers.Singleton(DefaultRoleRepo, storage.db_session)
