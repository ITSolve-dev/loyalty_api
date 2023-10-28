from typing import Optional, Sequence, Union

from pydantic import Field

from ..base import BaseSettings


class JwtSettings(BaseSettings):
    ACCESS_TOKEN_LIFETIME: int = Field(default=2, description="Expiration access token in minutes")
    REFRESH_TOKEN_LIFETIME: int = Field(default=1, description="Expiration refresh token in days")
    SIGNING_KEY: str = Field(default="secret", description="Secret key of sign of jwt")
    AUDIENCE: Union[str, Sequence[str]] = Field(default=[], description="Audience")
    ISSUER: str = Field(default="iss", description="Issuer")
    AUTO_ERROR: Optional[bool] = Field(default=False)
    PREFIX_HEADER: Optional[str] = Field(default=None, description="Prefix header for jwt")
    MAX_ACTIVE_SESSIONS: Optional[int] = Field(
        default=5, description="Max active login user's sessions"
    )
