import json
from unittest.mock import MagicMock

import pytest
from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.core.exception_handlers import (
    exception_handler,
    http_exception_handler,
    model_loading_exception_handler,
    prediction_exception_handler,
)
from app.core.exceptions import ModelLoadingError, PredictionError


@pytest.mark.anyio
class TestExceptionHandlers:
    async def test_model_loading_exception_handler(self):
        request = MagicMock(spec=Request)
        exc = ModelLoadingError(detail="Test Model Loading Error")
        response = await model_loading_exception_handler(request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert json.loads(response.body) == {"message": "Test Model Loading Error"}

    async def test_prediction_exception_handler(self):
        request = MagicMock(spec=Request)
        exc = PredictionError(detail="Test Prediction Error")
        response = await prediction_exception_handler(request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert json.loads(response.body) == {"message": "Test Prediction Error"}

    async def test_http_exception_handler(self):
        request = MagicMock(spec=Request)
        exc = HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
        response = await http_exception_handler(request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert json.loads(response.body) == {"detail": "Not Found"}

    async def test_generic_exception_handler(self):
        request = MagicMock(spec=Request)
        exc = ValueError("Something unexpected happened")
        response = await exception_handler(request, exc)
        assert isinstance(response, JSONResponse)
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert json.loads(response.body) == {"detail": "Internal Server Error"}
