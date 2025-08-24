from contextlib import asynccontextmanager

import pytest

from app.core.config import settings


@pytest.fixture(scope="session")
def anyio_backend():
    """
    Fixture to enable anyio backend for async tests.
    Required for httpx.AsyncClient with pytest.
    """
    return "asyncio"


@asynccontextmanager
async def null_lifespan(app):
    yield


@pytest.fixture(scope="function")
async def client():
    from app.main import app

    app.router.lifespan_context = null_lifespan

    from httpx import ASGITransport, AsyncClient

    """Fixture to create an AsyncClient for testing."""
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac


@pytest.fixture(scope="session")
def api_prefix():
    return settings.api_prefix
