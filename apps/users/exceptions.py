from fastapi import status

from core import DeclareModuleAppException, AlreadyExistsInstanceException


class UsersException(DeclareModuleAppException):
    MODULE = "users"


class RoleException(UsersException):
    MODULE = "users.role"


class UsersAlreadyExistsException(UsersException, AlreadyExistsInstanceException):
    STATUS_CODE = status.HTTP_409_CONFLICT
