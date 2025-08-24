import pytest
from httpx import AsyncClient


@pytest.mark.anyio
class TestMain:
    async def test_welcome_endpoint(self, client: AsyncClient, api_prefix: str):
        """
        Test the /welcome endpoint to ensure it returns the correct message and status code.
        """
        response = await client.get(f"{api_prefix}/welcome")

        assert response.status_code == 200
        assert "message" in response.json()
        assert (
            response.json()["message"] == "¡Bienvenido a la API de Predicción de Iris!"
        )
