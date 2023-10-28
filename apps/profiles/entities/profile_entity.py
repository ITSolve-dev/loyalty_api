from typing import Iterable
from pydantic import BaseModel

from apps.users.entities.role_entity import RoleType
from apps.users.entities.user_entity import UserEntity


class ProfileEntity(BaseModel):
    """
    Profile entity
    """

    user: UserEntity
    roles: Iterable[RoleType]
