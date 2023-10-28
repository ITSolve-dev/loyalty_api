from dependency_injector.wiring import Provide, inject
from fastapi import Depends

from core import VersionedAPIRouter, ErrorDetails

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


@router.post("", response_model=RetrieveUserSchema)
@inject
async def add_user_from_telegram(
    user_data: CreateUserSchema, user_cases: UserCases = Depends(Provide["user_app.user_cases"])
) -> RetrieveUserSchema:
    return await user_cases.create_user(data=user_data)
