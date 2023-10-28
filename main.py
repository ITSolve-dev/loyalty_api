import uvicorn
from loguru import logger

from core import get_application
from settings import settings

app = get_application()

if __name__ == "__main__":
    logger.info(f"Application is working on {settings.server.HOST}:{settings.server.PORT}\n")
    uvicorn.run(
        "main:app",
        reload=settings.server.RELOAD,
        host=settings.server.HOST,
        port=settings.server.PORT,
    )
