import os
from typing import TypedDict, Optional

from pydantic_settings import SettingsConfigDict

from .auth import JwtSettings
from .base import BaseSettings
from .project import DockerSettings, ProjectSettings, ServerSettings
from .storages import DatabaseSettings, RedisSettings

ENV: str = os.getenv("ENV")


class EnvPath(TypedDict):
    dev: str
    test: str
    prod: str


ENV_PATHS: EnvPath = {
    "dev": ".env",
    "test": ".env.test",
    "prod": ".env.prod",
}


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=ENV_PATHS.get(ENV, ".env"),
        env_file_encoding="utf-8",
    )

    ENV: str

    database: DatabaseSettings
    redis: RedisSettings
    project: ProjectSettings
    docker: DockerSettings
    server: ServerSettings
    jwt: Optional[JwtSettings] = JwtSettings()


settings = Settings()
