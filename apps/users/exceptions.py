from core import DeclareModuleAppException


class UsersException(DeclareModuleAppException):
    MODULE = "users"


class RoleException(UsersException):
    MODULE = "users.role"
