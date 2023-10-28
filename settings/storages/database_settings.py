from ..base import BaseSettings


class DatabaseSettings(BaseSettings):
    NAME: str
    USER: str
    PORT: int
    HOST: str
    PASSWORD: str
    LOG_ORM: bool
    POOL_SIZE: int
    MAX_OVERFLOW: int
