from dependency_injector.wiring import inject, Provide

from core import BaseCases
from apps.profiles.repos import DefaultProfileRepo
from apps.profiles.schemas import CreateProfileSchema, RetrieveUserWithProfileSchema

from ..schemas import CreateUserSchema
from ..repos import DefaultUserRepo


class UserCases(BaseCases[DefaultUserRepo]):
    @inject
    async def create_user(
        self,
        data: CreateUserSchema,
        profiles_repo: DefaultProfileRepo = Provide["profiles_app.profile_repo"],
    ) -> RetrieveUserWithProfileSchema:
        user = await self.repo.create(data=data)
        profile = await profiles_repo.create(data=CreateProfileSchema(user_id=user.id))
        return RetrieveUserWithProfileSchema(
            **user.model_dump(),
            profile=profile
        )
        return user
