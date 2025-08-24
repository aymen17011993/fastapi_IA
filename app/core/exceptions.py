from fastapi import HTTPException, status


class ModelLoadingError(HTTPException):
    def __init__(self, detail: str = "Error al cargar el modelo de predicción."):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
        )


class PredictionError(HTTPException):
    def __init__(self, detail: str = "Error al realizar la predicción."):
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail
        )
