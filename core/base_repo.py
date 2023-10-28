import sqlalchemy as sa
from abc import ABC
from typing import Protocol, Optional
from pydantic import BaseModel

from db.orm import start_session, Base

from sqlalchemy.ext.asyncio import async_sessionmaker


class BaseRepo(ABC):
    table = None

    def __init__(self, db_session: async_sessionmaker):
        self.db_session = db_session

    async def default_create_instance(self, data: BaseModel) -> Optional[Base]:
        async with start_session(self.db_session) as session:
            query = sa.insert(self.table).values(**data.model_dump()).returning(self.table)
            instance = (await session.scalar(query))
            return instance

    async def default_retrieve_instance(self, id: int) -> Optional[Base]:
        async with start_session(self.db_session) as session:
            query = sa.select(self.table).where(self.table.id == id)
            instance = await session.scalar(query)
            return instance


class ICreateRepo(Protocol):
    async def create(self, data: object) -> Optional[object]:
        """Create"""


class IRetrieveRepo(Protocol):
    async def retrieve(self, id: int) -> Optional[object]:
        """Retrieve"""


class IUpdateRepo(Protocol):
    async def update(self, data: object) -> Optional[object]:
        """Update"""


class IDeleteRepo(Protocol):
    async def delete(self, id: int) -> Optional[object]:
        """Delete"""
