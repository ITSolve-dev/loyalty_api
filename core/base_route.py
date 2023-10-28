from typing import Callable, Coroutine, Any

from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response


class BaseRoute(APIRoute):
    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        return super().get_route_handler()
