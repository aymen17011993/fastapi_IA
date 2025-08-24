import logging
import os

import joblib
import numpy as np

from app.core.config import settings  # Importar settings
from app.core.exceptions import ModelLoadingError, PredictionError

logger = logging.getLogger(__name__)

MODEL_PATH = settings.model_path

_model = None


def load_model():
    """Carga el modelo entrenado desde el disco."""
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            logger.error(f"Modelo no encontrado en: {MODEL_PATH}")
            raise ModelLoadingError(
                detail=f"Modelo no encontrado en: {MODEL_PATH}. Por favor, entrena el modelo primero."
            )
        try:
            logger.info(f"Cargando modelo desde: {MODEL_PATH}")
            _model = joblib.load(MODEL_PATH)
            logger.info("Modelo cargado exitosamente.")
        except Exception as e:
            logger.error(f"Error al cargar el modelo desde {MODEL_PATH}: {e}")
            raise ModelLoadingError(detail=f"Error al cargar el modelo: {e}") from e
    return _model


def predict_iris(features: list[float]) -> int:
    """Realiza una predicción usando el modelo cargado."""
    model = load_model()
    # Convertir la lista de características a un array de numpy y reformar para el modelo
    features_array = np.array(features).reshape(1, -1)
    try:
        prediction = model.predict(features_array)
        return int(prediction[0])
    except Exception as e:
        logger.error(f"Error al realizar la predicción: {e}")
        raise PredictionError(detail=f"Error al realizar la predicción: {e}") from e
