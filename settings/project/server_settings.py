from ..base import BaseSettings


class ServerSettings(BaseSettings):
    PORT: int
    HOST: str
    RELOAD: bool
    WORKERS: int
