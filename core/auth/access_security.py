from datetime import timedelta
from typing import Any, Dict, List, Optional, Union

from fastapi_jwt import JwtAccessBearerCookie


class ExtendedPayloadAccess(JwtAccessBearerCookie):
    def __init__(self, iss: str, aud: Union[str, List[str]], *args, **kwargs):
        self.iss = iss
        self.aud = aud.split(",") if isinstance(aud, str) else aud
        super().__init__(*args, **kwargs)

    def _generate_payload(
        self,
        subject: Dict[str, Any],
        expires_delta: timedelta,
        unique_identifier: str,
        token_type: str,
    ) -> Dict[str, Any]:
        payload = super()._generate_payload(subject, expires_delta, unique_identifier, token_type)
        return dict(**payload, iss=self.iss, aud=self.aud)


def create_access_security(
    secret_key: str,
    iss: str,
    aud: Union[str, List[str]],
    auto_error: bool = False,
    access_expires_delta: Optional[int] = None,
    refresh_expires_delta: Optional[int] = None,
):
    return ExtendedPayloadAccess(
        iss=iss,
        aud=aud,
        secret_key=secret_key,
        auto_error=auto_error,
        access_expires_delta=timedelta(minutes=access_expires_delta),
        refresh_expires_delta=timedelta(days=refresh_expires_delta),
    )
