from ..base import BaseSettings
from .docs_settings import DocsSettings


class ProjectSettings(BaseSettings):
    NAME: str
    VERSION: str
    API_VERSIONS: str
    docs: DocsSettings
