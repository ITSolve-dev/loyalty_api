from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Body

from core import VersionedAPIRouter, ErrorDetails
from apps.scans.schemas import ListScanSchema
from apps.scans.cases import ScansCases

from ..schemas import *
from ..cases import ProfileCases

router = VersionedAPIRouter(
    v=1, prefix="/profiles", tags=["profiles"], responses={404: {"model": ErrorDetails}}
)


@router.post("", response_model=RetrieveProfileSchema)
@inject
async def create_profile(
    profile_data: CreateProfileSchema,
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
):
    return await profile_cases.create(data=profile_data)


@router.get("/{profile_id}", response_model=RetrieveProfileSchema)
@inject
async def get_detailed_profile(
    profile_id: int,
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
):
    return await profile_cases.retrieve(profile_id=profile_id)


@router.post("/{profile_id}/roles", response_model=RetrieveProfileSchema)
@inject
async def add_roles_to_profile(
    profile_id: int,
    data: AddProfileRolesSchema = Body(),
    profile_cases: ProfileCases = Depends(Provide["profiles_app.profile_cases"]),
):
    return await profile_cases.add_roles(profile_id=profile_id, data=data)


@router.get("/{profile_id}/scans", response_model=ListScanSchema)
@inject
async def add_roles_to_profile(
    profile_id: int,
    scans_cases: ScansCases = Depends(Provide["scans_app.scans_cases"]),
):
    return await scans_cases.get_scans_profile(id=profile_id)
