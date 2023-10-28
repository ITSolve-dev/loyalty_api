from dependency_injector import containers, providers

from .orm import create_async_session, Session, get_session
from .redis import create_redis


class StorageContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    db_session = providers.Resource(Session)
    # db_session = providers.Resource(get_session)

    redis_cache = providers.Resource(create_redis, host=config.redis.HOST, port=config.redis.PORT)
