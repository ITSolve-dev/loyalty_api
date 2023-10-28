import sys
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from settings import settings

Base = declarative_base()

engine = create_async_engine(
    f"postgresql+asyncpg://{settings.database.USER}:{settings.database.PASSWORD}@{settings.database.HOST}:{settings.database.PORT}/{settings.database.NAME}",
    # More detailed logging is mentioned here
    # https://stackoverflow.com/questions/48812971/flask-sqlalchemy-advanced-logging
    echo=settings.database.LOG_ORM,
    pool_size=100,
    max_overflow=0,
)

Session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


def get_session() -> async_sessionmaker:
    return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@asynccontextmanager
async def start_session(session: AsyncSession) -> AsyncSession:
    trans = None
    nested = False
    try:
        nested = session.in_transaction()
        if nested:
            trans = session.begin_nested()
        else:
            trans = session.begin()

        await trans.__aenter__()
        yield session
    finally:
        if trans:
            await trans.__aexit__(*sys.exc_info())
        if not nested:
            await session.__aexit__(*sys.exc_info())


def create_async_session(
    user: str,
    password: str,
    host: str,
    port: int,
    name: str,
    echo: bool,
    pool_size: int,
    max_overflow: int,
) -> async_sessionmaker:
    async_engine = create_async_engine(
        f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}",
        echo=echo,
        pool_size=pool_size,
        max_overflow=max_overflow,
    )
    return async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
