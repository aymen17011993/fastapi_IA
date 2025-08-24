import asyncio
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.routers import prediction

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        yield
    except (asyncio.CancelledError, KeyboardInterrupt):
        pass


app = FastAPI(
    title=settings.app_name,
    description=settings.app_description,
    version=settings.api_version,
    contact=settings.app_contact.model_dump(),
    docs_url=settings.app_docs_url,
    redoc_url=settings.app_redoc_url,
    lifespan=lifespan,
)


register_exception_handlers(app)

app.include_router(prediction.router, prefix=settings.api_prefix)


@app.get(f"{settings.api_prefix}/welcome", tags=["Welcome"])
async def read_root():
    return {"message": "¡Bienvenido a la API de Predicción de Iris!"}
