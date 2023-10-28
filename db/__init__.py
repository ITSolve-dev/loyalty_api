from settings import settings

from .containers import StorageContainer
from .orm import Base

StorageContainer.config.from_dict(settings.model_dump())

__all__ = (
    "Base",
    "StorageContainer",
)
