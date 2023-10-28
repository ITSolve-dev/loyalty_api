from dependency_injector import containers, providers

from db import StorageContainer

from .users.container import Container as UserContainer
from .profiles.containers import Container as ProfileContainer
from .institutions.containers import Container as InstitutionContainer
from .scans.containers import Container as ScansContainer

storage_container = StorageContainer()
storage_container.wire(packages=[__name__])


class RootContainer(containers.DeclarativeContainer):
    storage = providers.Container(StorageContainer)
    user_app = providers.Container(UserContainer, storage=storage)
    profiles_app = providers.Container(ProfileContainer, storage=storage)
    institutions_app = providers.Container(InstitutionContainer, storage=storage)
    scans_app = providers.Container(ScansContainer, storage=storage)


root_container = RootContainer()
root_container.wire(packages=[__name__])
