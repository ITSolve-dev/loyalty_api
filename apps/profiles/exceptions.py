from fastapi import status
from core import (
    DeclareModuleAppException,
    NotFoundInstanceException,
    AlreadyExistsInstanceException,
)


class ProfilesException(DeclareModuleAppException):
    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    MODULE = "profiles"


class ProfileNotFoundException(ProfilesException, NotFoundInstanceException):
    pass


class ProfileAlreadyExistsException(ProfilesException, AlreadyExistsInstanceException):
    pass


class ProfileRolesExistException(ProfilesException):
    ERROR = "exist_roles"
    DESCRIPTION = "All that roles already exist in that profile"
