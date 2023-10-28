from typing import Sequence

from core import BaseRepo, ICreateRepo, IRetrieveRepo

from ..models import Scan
from ..schemas import *


class IScansRepo(BaseRepo, ICreateRepo, IRetrieveRepo):
    table = Scan

    async def get_scans_profile(self, profile_id: int) -> Sequence[ScanSchema]:
        raise NotImplemented
