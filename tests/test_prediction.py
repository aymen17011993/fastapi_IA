import pytest
from httpx import AsyncClient


@pytest.mark.anyio
class TestPrediction:
    async def test_predict_endpoint(self, client: AsyncClient, api_prefix: str):
        """
        Test the /predict/ endpoint with valid input.
        """
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        }
        response = await client.post(f"{api_prefix}/predict/", json=payload)

        assert response.status_code == 200
        assert "predicted_class" in response.json()
        assert "class_name" in response.json()
        assert isinstance(response.json()["predicted_class"], int)
        assert isinstance(response.json()["class_name"], str)

    async def test_predict_endpoint_invalid_input(
        self, client: AsyncClient, api_prefix: str
    ):
        """
        Test the /predict/ endpoint with invalid input (missing fields).
        """
        payload = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
        }
        response = await client.post(f"{api_prefix}/predict/", json=payload)

        assert response.status_code == 422  # Unprocessable Entity for validation errors
        assert "detail" in response.json()
        assert isinstance(response.json()["detail"], list)
        assert len(response.json()["detail"]) > 0
