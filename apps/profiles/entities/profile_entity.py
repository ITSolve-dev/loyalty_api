from pydantic import BaseModel

from apps.users.entities.user_entity import UserEntity
from .role_entity import RoleType


class ProfileEntity(BaseModel):
    """
    Profile entity
    """

    user: UserEntity
    role: RoleType
