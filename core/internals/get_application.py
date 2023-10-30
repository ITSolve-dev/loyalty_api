from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI
from starlette.middleware.cors import CORSMiddleware

from settings import settings

from .decorate_fast_api import decorate_fast_api
from .get_routers import GetRouters


def get_application() -> FastAPI:
    """
    Makes Fast API instance,
    Add middlewares,
    Import all routers and are in router_<x>.py files
    """

    app = FastAPI(
        title=settings.project.NAME,
        description=settings.project.docs.DESCRIPTION,
        version=settings.project.VERSION,
        summary=settings.project.docs.SUMMARY,
    )

    for version in settings.project.API_VERSIONS.split(","):
        routers = GetRouters.call(version)
        for router in routers:
            app.include_router(router["value"])

    v_app = VersionedFastAPI(
        app,
        version_format="{major}",
        prefix_format="/api/v{major}",
        enable_latest=True,
    )

    # decorate Fast API application with some additional handlers for events, requests, etc
    decorate_fast_api(v_app)
    v_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return v_app
