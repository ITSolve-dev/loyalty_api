from typing import Callable

from fastapi import Request, Response

from settings import settings

from ..base_route import BaseRoute


class TokenFormatException(Exception):
    pass


class PrefixJwtTokenException(Exception):
    pass


class AuthRoute(BaseRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            auth_header = request.headers.get("authorization", None)
            if auth_header:
                try:
                    prefix, token = auth_header.split(" ")
                except Exception as e:
                    raise TokenFormatException(e)
                else:
                    if prefix != settings.jwt.PREFIX_HEADER:
                        raise PrefixJwtTokenException("Prefix error")

            response = await original_route_handler(request)
            return response

        return custom_route_handler
