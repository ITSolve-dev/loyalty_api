from core import BaseCases

from ..repos import DefaultScansRepo
from ..schemas import *


class ScansCases(BaseCases[DefaultScansRepo]):
    async def create(self, data: CreateScanSchema) -> RetrieveScanSchema:
        return await self.repo.create(data=data)

    async def retrieve(self, id: int) -> RetrieveScanSchema:
        return await self.repo.retrieve(id=id)

    async def get_scans_profile(self, id: int) -> ListScanSchema:
        return await self.repo.get_scans_profile(profile_id=id)

    async def get_scanned_profile(self, id: int) -> ListScanSchema:
        return await self.repo.get_scanned_profile(profile_id=id)
