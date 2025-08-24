import logging
import os

import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

MODEL_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "app", "model_artifacts"
)
MODEL_PATH = os.path.join(MODEL_DIR, "model.joblib")

os.makedirs(MODEL_DIR, exist_ok=True)

logger.info("Cargando el dataset Iris...")
iris = load_iris()
X, y = iris.data, iris.target

logger.info("Entrenando un modelo de Regresión Logística...")
model = LogisticRegression(max_iter=200, solver="lbfgs")
model.fit(X, y)

logger.info(f"Guardando el modelo entrenado en '{MODEL_PATH}'...")
joblib.dump(model, MODEL_PATH)

logger.info("Modelo entrenado y guardado exitosamente.")
logger.info(f"Puedes verificar que el archivo '{MODEL_PATH}' ha sido creado.")
