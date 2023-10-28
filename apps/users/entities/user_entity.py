from typing import Optional

from pydantic import BaseModel


class UserEntity(BaseModel):
    """
    User entity
    """

    telegram_id: int
    username: Optional[str]
    first_name: str
