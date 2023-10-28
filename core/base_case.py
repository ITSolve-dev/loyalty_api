from abc import ABC
from typing import Generic, TypeVar, Callable, Type, Union

from pydantic import ValidationError
from loguru import logger

from .exceptions import AppException

RepoType = TypeVar("RepoType")


def handle_validation_exc(ValidationException: Union[Type[AppException], AppException]):
    def wrapper(method: Callable):
        async def func(*args, **kwargs):
            try:
                return await method(*args, **kwargs)
            except ValidationError as e:
                logger.error(e)
                raise ValidationException

        return func

    return wrapper


class BaseCases(ABC, Generic[RepoType]):
    def __init__(self, repo: RepoType):
        self._repo = repo

    @property
    def repo(self) -> RepoType:
        return self._repo
