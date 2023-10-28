from fastapi import Depends, Request, status

# from apps.auth.exceptions import AuthNotAuthorizedException
from fastapi.security import HTTPBearer

from core import AppException


def get_current_user(request: Request) -> dict:
    return request.state.user


class IsAuthenticated(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    def __call__(self, user: dict = Depends(get_current_user)):
        if not user:
            raise AppException(
                error="auth.not_authorized",
                description="Not authorized",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return user


def is_active():
    pass


def is_admin():
    pass
