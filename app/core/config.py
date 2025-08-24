import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Contact(BaseModel):
    name: str
    url: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "API de Predicción de Iris"
    app_description: str = "Una API simple para predecir la especie de flor Iris."
    app_version: str = "1"
    app_contact: Contact = Contact(
        name="Víctor García", url="https://github.com/vicogarcia16"
    )
    app_docs_url: str = "/"
    app_redoc_url: str = "/redoc"

    model_path: str = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "model_artifacts",
        "model.joblib",
    )

    @property
    def api_prefix(self):
        return f"/api/v{self.app_version}"

    @property
    def api_version(self):
        return f"{self.app_version}.0.0"


settings = Settings()
