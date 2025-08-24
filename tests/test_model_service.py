from unittest.mock import MagicMock, patch

import pytest

from app.core.exceptions import ModelLoadingError, PredictionError
from app.services.model_service import load_model, predict_iris


class TestModelService:
    def test_load_model_file_not_found(self, monkeypatch: pytest.MonkeyPatch):
        """
        Test that ModelLoadingError is raised when the model file does not exist.
        """
        monkeypatch.setattr(
            "app.services.model_service._model", None
        )  # Reset the global model variable
        with patch("os.path.exists", return_value=False):
            with pytest.raises(ModelLoadingError) as excinfo:
                load_model()
            assert "Modelo no encontrado" in str(excinfo.value)

    def test_load_model_failure(self, monkeypatch: pytest.MonkeyPatch):
        """
        Test that ModelLoadingError is raised when joblib.load fails.
        """
        monkeypatch.setattr(
            "app.services.model_service._model", None
        )  # Reset the global model variable
        with patch("os.path.exists", return_value=True):
            with patch("joblib.load", side_effect=Exception("Corrupted model")):
                with pytest.raises(ModelLoadingError) as excinfo:
                    load_model()
                assert "Error al cargar el modelo" in str(excinfo.value)

    def test_predict_iris_failure(self, monkeypatch: pytest.MonkeyPatch):
        """
        Test that PredictionError is raised when model.predict fails.
        """
        mock_model = MagicMock()
        mock_model.predict.side_effect = Exception("Prediction failed")
        monkeypatch.setattr("app.services.model_service.load_model", lambda: mock_model)

        with pytest.raises(PredictionError) as excinfo:
            predict_iris([1.0, 2.0, 3.0, 4.0])
        assert "Error al realizar la predicción" in str(excinfo.value)
