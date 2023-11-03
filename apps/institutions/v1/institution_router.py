from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Body

from core import VersionedAPIRouter, ErrorDetails

from ..schemas import *
from ..cases import InstitutionCases

router = VersionedAPIRouter(
    v=1, prefix="/institutions", tags=["institutions"], responses={404: {"model": ErrorDetails}}
)


@router.post("", response_model=RetrieveInstitutionSchema, operation_id="createInstitution")
@inject
async def create_institution(
    data: CreateInstitutionSchema,
    institution_cases: InstitutionCases = Depends(Provide["institutions_app.institution_cases"]),
) -> RetrieveInstitutionSchema:
    return await institution_cases.create(data=data)


@router.get("/{id}", response_model=RetrieveInstitutionSchema, operation_id="getInstitutionById")
@inject
async def get_institution_by_id(
    id: int,
    institution_cases: InstitutionCases = Depends(Provide["institutions_app.institution_cases"]),
) -> RetrieveInstitutionSchema:
    return await institution_cases.retrieve(id=id)


@router.post(
    "/{id}/users", response_model=RetrieveInstitutionSchema, operation_id="addUsersToInstitution"
)
@inject
async def add_users_to_institution(
    id: int,
    data: AddUsersInstitutionSchema = Body(),
    institution_cases: InstitutionCases = Depends(Provide["institutions_app.institution_cases"]),
):
    return await institution_cases.add_users(id=id, user_ids=data.user_ids)


@router.get(
    "/profile/{profile_id}",
    response_model=ListInstitutionSchema,
    operation_id="getInstitutionsByCustomerProfileId",
)
@inject
async def get_institutions_by_customer_profile_id(
    profile_id: int,
    institution_cases: InstitutionCases = Depends(Provide["institutions_app.institution_cases"]),
):
    return await institution_cases.get_by_customer_profile_id(profile_id=profile_id)
