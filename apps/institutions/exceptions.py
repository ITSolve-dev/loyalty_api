from fastapi import status

from core import (
    DeclareModuleAppException,
    NotFoundInstanceException,
    ValidationDataInstanceException,
)


class InstitutionsException(DeclareModuleAppException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    MODULE = "institutions"


class InstitutionNotFoundException(InstitutionsException, NotFoundInstanceException):
    pass


class InstitutionValidationException(InstitutionsException, ValidationDataInstanceException):
    pass


class InstitutionAddUsersNotExistsException(InstitutionsException):
    ERROR = "not_exist_ids"
    DESCRIPTION = "Such user ids does not exist"
