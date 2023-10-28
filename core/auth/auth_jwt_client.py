from typing import Any, Callable, Dict, Literal, Optional

import jwt
from fastapi import status
from jwt import ExpiredSignatureError
from loguru import logger
from pydantic import BaseModel

from core import AppException

from .access_security import ExtendedPayloadAccess

ClaimType = Dict[str, Any]
TokenType = Literal["access", "refresh"]


class PayloadSchema(BaseModel):
    pass


class AuthJwtClient:
    def __init__(self, access_security: ExtendedPayloadAccess):
        self.access_security = access_security

    def __get_action(self, type: TokenType) -> Callable:
        config = {
            "access": self.access_security.create_access_token,
            "refresh": self.access_security.create_refresh_token,
        }
        return config.get(type, self.access_security.create_access_token)

    def create_access_token(self, claim: ClaimType, *args, **kwargs) -> str:
        return self._create_token(claim, type="access", *args, **kwargs)

    def create_refresh_token(self, claim: ClaimType, *args, **kwargs) -> str:
        return self._create_token(claim, type="refresh", *args, **kwargs)

    def _create_token(self, claims: ClaimType, type: TokenType, *args, **kwargs) -> str:
        return self.__get_action(type)(subject=claims, *args, **kwargs)

    def generate_pair(self, data: ClaimType) -> dict:
        return {
            "access_token": self.create_access_token(claim=data),
            "refresh_token": self.create_refresh_token(claim=data),
        }

    def decode_token(self, token: str, extra_info: bool = False) -> Optional[dict]:
        if token:
            header_data = jwt.get_unverified_header(token)
            try:
                payload = jwt.decode(
                    token,
                    audience=self.access_security.aud,
                    key=self.access_security.secret_key,
                    algorithms=[
                        header_data.get("alg", self.access_security.algorithm),
                    ],
                )
            except ExpiredSignatureError as e:
                raise AppException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    error="auth.token_expired",
                    description=str(e),
                )
            except Exception as e:
                logger.error(e)
                payload = None

            if not payload:
                raise AppException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    error="auth.token_invalid",
                )

            return payload if extra_info else payload.get("subject", {})

        return None
