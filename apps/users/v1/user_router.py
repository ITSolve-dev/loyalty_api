from pprint import pformat

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Body
from loguru import logger

from core import VersionedAPIRouter, ErrorDetails
from  apps.profiles.schemas import RetrieveUserWithProfileSchema

from ..schemas import *
from ..cases import *

router = VersionedAPIRouter(
    v=1,
    prefix="/users",
    tags=["users"],
    responses={
        404: {"model": ErrorDetails},
    },
)


@router.post("", response_model=RetrieveUserWithProfileSchema)
@inject
async def add_user_from_telegram(
    user_data: CreateUserSchema = Body(), user_cases: UserCases = Depends(Provide["user_app.user_cases"])
) -> RetrieveUserWithProfileSchema:
    logger.info(pformat(user_data))
    return await user_cases.create_user(data=user_data)
