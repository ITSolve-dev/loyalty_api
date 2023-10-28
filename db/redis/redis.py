from typing import Optional

from aioredis import Redis, from_url


async def create_redis(host: str, port: int, password: Optional[str] = None) -> Redis:
    redis_session = from_url(
        url=f"redis://{host}:{port}", encoding="utf-8", decode_responses=True, password=password
    )
    yield redis_session
    redis_session.close()
    await redis_session.wait_closed()
