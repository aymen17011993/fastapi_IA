from pydantic import BaseModel, ConfigDict


class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "sepal_length": 5.1,
                    "sepal_width": 3.5,
                    "petal_length": 1.4,
                    "petal_width": 0.2,
                }
            ]
        }
    }


class PredictionResult(BaseModel):
    predicted_class: int
    class_name: str
    model_config = ConfigDict(from_attributes=True)
