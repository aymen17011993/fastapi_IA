from fastapi import APIRouter

from app.core.constants import IRIS_CLASSES
from app.schemas.prediction import IrisFeatures, PredictionResult
from app.services.model_service import predict_iris

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=PredictionResult)
async def predict(features: IrisFeatures):
    """
    Realiza una predicción de la especie de Iris basándose en las características proporcionadas.
    """
    features_list = [
        features.sepal_length,
        features.sepal_width,
        features.petal_length,
        features.petal_width,
    ]

    predicted_class_id = predict_iris(features_list)
    predicted_class_name = IRIS_CLASSES.get(predicted_class_id, "Desconocido")

    return PredictionResult(
        predicted_class=predicted_class_id, class_name=predicted_class_name
    )
