# API de Predicción de Iris con FastAPI 🌸

Este proyecto implementa una API sencilla para servir un modelo de aprendizaje automático utilizando FastAPI. La API predice la especie de la flor de Iris basándose en las características proporcionadas. 🚀

## Características ✨

-   **FastAPI**: Un framework web moderno, rápido y de alto rendimiento para construir APIs con Python 3.7+ basado en las sugerencias de tipo estándar de Python. ⚡
-   **Scikit-learn**: Utilizado para el modelo de clasificación de Iris. 📊
-   **Pipenv**: Para la gestión de dependencias y la definición de scripts convenientes. 📦
-   **Docker**: Para la contenerización y un despliegue sencillo. 🐳
-   **Tests Unitarios**: Tests unitarios completos con buena cobertura. ✅
-   **Manejo de Excepciones**: Manejadores de excepciones personalizados para respuestas robustas de la API. 🛡️
-   **Ruff**: Un linter y formateador de código extremadamente rápido para Python. 🧹

## Estructura del Proyecto 📁

```
.fastapi_IA/
├── app/
│   ├── core/             # Configuraciones principales, constantes, excepciones y manejadores
│   ├── model_artifacts/  # Directorio para almacenar el modelo entrenado
│   ├── routers/          # Rutas de la API (ej. endpoint de predicción)
│   ├── schemas/          # Modelos Pydantic para validación de solicitudes/respuestas
│   └── services/         # Lógica de negocio e interacción con el modelo
├── scripts/              # Scripts para el entrenamiento del modelo
├── tests/                # Tests unitarios
├── Dockerfile            # Instrucciones de construcción de Docker
├── docker-compose.yml    # Configuración de Docker Compose
├── Pipfile               # Archivo de dependencias de Pipenv
├── Pipfile.lock          # Archivo de bloqueo de Pipenv
└── README.md             # README del proyecto
```

## Configuración e Instalación 🛠️

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/your-username/fastapi_IA.git
    cd fastapi_IA
    ```

2.  **Instalar dependencias usando Pipenv:**

    Si no tienes Pipenv instalado, puedes instalarlo a través de pip:
    ```bash
    pip install pipenv
    ```

    Luego, instala las dependencias del proyecto. Puedes usar la configuración de `Pipfile` directamente:
    ```bash
    pipenv install
    ```

3.  **Activar el shell de Pipenv:**

    ```bash
    pipenv shell
    ```

4.  **Entrenar el modelo:**

    Antes de ejecutar la API, necesitas entrenar el modelo de aprendizaje automático. Esto generará el archivo `model.joblib` en `app/model_artifacts/`.
    ```bash
    python scripts/train_model.py
    ```

## Ejecutar la Aplicación ▶️

Una vez que las dependencias estén instaladas y el modelo entrenado, puedes ejecutar la aplicación FastAPI usando el script definido en `Pipfile`:

```bash
# Asegúrate de estar en el shell de pipenv (paso 3 anterior)
pipenv run server
```

La API será accesible en `http://localhost:8000`.

## Ejecutar Tests 🧪

Para ejecutar los tests unitarios y verificar la cobertura del código usando los scripts definidos en `Pipfile`:

```bash
# Asegúrate de estar en el shell de pipenv
pipenv run test-cov
```

## Uso de Ruff 🐶

Este proyecto utiliza [Ruff](https://beta.ruff.rs/docs/) para el linting y formateo del código, asegurando la calidad y consistencia del mismo. Puedes ejecutar Ruff usando los scripts definidos en `Pipfile`:

```bash
# Para verificar errores de linting
pipenv run lint

# Para corregir automáticamente los errores de linting (donde sea posible)
pipenv run fix

# Para formatear el código
pipenv run format
```

## Docker 🐳

También puedes construir y ejecutar la aplicación usando Docker para la contenerización.

1.  **Construir la imagen de Docker:**

    ```bash
    docker-compose build
    ```

2.  **Ejecutar la aplicación con Docker Compose:**

    ```bash
    docker-compose up
    ```

    La aplicación estará disponible en `http://localhost:8000`.

3.  **Detener la aplicación (Docker Compose):**

    Para detener los contenedores en ejecución:
    ```bash
    docker-compose down
    ```

## Endpoints de la API 🌐

-   **`/api/v1/welcome` (GET)**: Un endpoint de bienvenida. 👋
-   **`/api/v1/predict/` (POST)**: Predice la especie de Iris basándose en las características de entrada. 🔮
    -   **Ejemplo de Cuerpo de Solicitud (`application/json`):**
        ```json
        {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        ```
    -   **Ejemplo de Cuerpo de Respuesta (`application/json`):**
        ```json
        {
            "predicted_class": 0,
            "class_name": "setosa"
        }
        ```

Para la documentación detallada de la API (Swagger UI), visita `http://localhost:8000/` cuando la aplicación esté en ejecución.

## Licencia 📄

Este proyecto está bajo la Licencia MIT. Fue desarrollado por [vicogarcia16](https://github.com/vicogarcia16). Consulta el archivo LICENSE para más detalles.