from fastapi import APIRouter
from fastapi_versioning import version


class VersionedAPIRouter(APIRouter):
    def __init__(self, v, *args, **kwargs):
        self.v = v
        super().__init__(*args, **kwargs)

    def api_route(self, *args, **kwargs):
        return version(self.v)(super().api_route(*args, **kwargs))


VersionedAPIRouter.__init__.__annotations__ = VersionedAPIRouter.__init__.__annotations__.update(
    APIRouter.__init__.__annotations__
)
