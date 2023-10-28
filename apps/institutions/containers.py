from dependency_injector import containers, providers

from .repos import DefaultInstitutionRepo, DefaultInstitutionTypeRepo, DefaultMemberRepo
from .cases import InstitutionCases


class Container(containers.DeclarativeContainer):
    storage = providers.DependenciesContainer()

    institution_type_repo = providers.Singleton(DefaultInstitutionTypeRepo, storage.db_session)
    institution_repo = providers.Singleton(DefaultInstitutionRepo, storage.db_session)
    members_repo = providers.Singleton(DefaultMemberRepo, storage.db_session)

    institution_cases = providers.Singleton(InstitutionCases, institution_repo)
