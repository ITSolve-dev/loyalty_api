import os
from typing import Dict, List, Optional

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import TypeAdapter

from core import ErrorDetails


class AppException(HTTPException):
    def __init__(
        self,
        error: str,
        description: Optional[str] = None,
        ctx: Optional[Dict] = None,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ):
        ta = TypeAdapter(List[ErrorDetails])
        errors = ta.validate_python([{"type": error, "description": description, "ctx": ctx}])
        super().__init__(
            status_code=status_code, detail=jsonable_encoder(errors, exclude_none=True)
        )


class DeclareModuleAppException(AppException):
    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    MODULE: str
    ERROR: str
    DESCRIPTION: Optional[str] = None

    def __init__(self, message: Optional[str] = None, ctx: Optional[Dict] = None):
        super().__init__(
            status_code=self.STATUS_CODE,
            description=message or self.DESCRIPTION or "",
            error=f"{self.MODULE}.{self.ERROR}",
            ctx=ctx,
        )


class NotFoundInstanceException(DeclareModuleAppException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    ERROR = "not_found"
    DESCRIPTION = "Server can not find such instance"


class AlreadyExistsInstanceException(DeclareModuleAppException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    ERROR = "already_exists"
    DESCRIPTION = "Such instance exists"


class ValidationDataInstanceException(DeclareModuleAppException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    ERROR = "validation_data"
    DESCRIPTION = "Wrong data sent"


class UnknownException(DeclareModuleAppException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    ERROR = "unknown"
    DESCRIPTION = "Something went wrong"

    def __init__(self, module: str, ctx: Optional[Dict] = None):
        self.MODULE = module
        super().__init__(ctx=ctx)
