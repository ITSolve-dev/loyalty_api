from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from loguru import logger
from pprint import pformat

from core import VersionedAPIRouter, ErrorDetails, BaseRoute
from apps.scans.schemas import ListScanSchema
from apps.scans.cases import ScansCases

from ..schemas import *
from ..cases import ProfileCases

router = VersionedAPIRouter(
    v=1,
    prefix="/profiles",
    tags=["profiles"],
    responses={404: {"model": ErrorDetails}},
    route_class=BaseRoute,
)


@router.post("", response_model=RetrieveProfileSchema, operation_id="createProfile")
@inject
async def create_profile(
    profile_data: CreateProfileSchema,
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
):
    return await profile_cases.create(data=profile_data)


@router.get("/{profile_id}", response_model=RetrieveProfileSchema, operation_id="getProfileById")
@inject
async def get_profile_by_id(
    profile_id: int,
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
):
    return await profile_cases.retrieve(profile_id=profile_id)


@router.get(
    "/telegram/{telegram_id}",
    response_model=list[RetrieveProfileSchema],
    operation_id="getProfilesByTelegramId",
)
@inject
async def get_profiles_by_telegram_id(
    telegram_id: int,
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
) -> list[RetrieveProfileSchema]:
    result = await profile_cases.get_profiles_by_telegram_id(telegram_id=telegram_id)
    return result


@router.get(
    "/{profile_id}/scans", response_model=ListScanSchema, operation_id="getScansByProfileId"
)
@inject
async def get_scans_by_profile_id(
    profile_id: int,
    scans_cases: ScansCases = Depends(Provide["scans_app.scans_cases"]),
):
    return await scans_cases.get_scans_profile(id=profile_id)


@router.get(
    "/{profile_id}/scanned", response_model=ListScanSchema, operation_id="getScannedByProfileId"
)
@inject
async def get_scanned_by_profile_id(
    profile_id: int,
    scans_cases: ScansCases = Depends(Provide["scans_app.scans_cases"]),
):
    return await scans_cases.get_scanned_profile(id=profile_id)
