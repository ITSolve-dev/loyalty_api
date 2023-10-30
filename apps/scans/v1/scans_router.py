from pprint import pformat

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, Body
from loguru import logger

from core import VersionedAPIRouter, ErrorDetails

from ..schemas import *
from ..cases import ScansCases

router = VersionedAPIRouter(
    v=1, prefix="/scans", tags=["scans"], responses={404: {"model": ErrorDetails}}
)


@router.post("", response_model=RetrieveScanSchema)
@inject
async def create_scan(
    data: CreateScanSchema = Body(), scans_cases: ScansCases = Depends(Provide["scans_app.scans_cases"])
) -> RetrieveScanSchema:
    logger.info(pformat(data))
    return await scans_cases.create(data=data)


@router.get("/{scan_id}", response_model=RetrieveScanSchema)
@inject
async def get_detailed_scan(
    scan_id: int, scans_cases: ScansCases = Depends(Provide["scans_app.scans_cases"])
):
    return await scans_cases.retrieve(id=scan_id)
