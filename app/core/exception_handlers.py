from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse

from app.core.exceptions import ModelLoadingError, PredictionError


async def model_loading_exception_handler(request: Request, exc: ModelLoadingError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def prediction_exception_handler(request: Request, exc: PredictionError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code, content={"detail": exc.detail or "HTTP Error"}
    )


async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"},
    )


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(ModelLoadingError, model_loading_exception_handler)
    app.add_exception_handler(PredictionError, prediction_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, exception_handler)
