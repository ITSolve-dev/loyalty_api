from typing import Optional

from ..base import BaseSettings


class RedisSettings(BaseSettings):
    HOST: str
    PORT: int
    PASSWORD: Optional[str] = None
