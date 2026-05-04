"""
ABC Analytics - Sales Prediction API.

REST API for sales prediction service migrated from on-premise to Azure.
Implements DevOps best practices: structured logging, health checks, and
confidence level classification.

Author: Juan Manuel Campos Enrique / Mónica Penacho
Version: 1.0.0
"""

import logging
import time
import os
import random
from fastapi import FastAPI
from app.models import SalesPrediction, PredictionResponse

# Configure structured logging for production observability
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

# App version injected via environment variable (set in Dockerfile/Terraform)
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(
    title="ABC Analytics - Sales Prediction API",
    description="API de predicción de ventas migrada a Azure",
    version=APP_VERSION
)


def _nivel_confianza(confidence: float) -> str:
    """Classify prediction confidence into risk levels.

    Args:
        confidence: Float between 0 and 1 representing prediction confidence.

    Returns:
        String label: 'ALTO' (≥0.90), 'MEDIO' (≥0.80), or 'BAJO' (<0.80).

    Example:
        >>> _nivel_confianza(0.92)
        'ALTO'
        >>> _nivel_confianza(0.85)
        'MEDIO'
    """
    if confidence >= 0.90:
        return "ALTO"
    elif confidence >= 0.80:
        return "MEDIO"
    return "BAJO"


@app.get("/")
def root():
    """Root endpoint — confirms the API is running.

    Returns:
        JSON with welcome message and current API version.
    """
    return {
        "message": "ABC Analytics API funcionando en Azure",
        "version": APP_VERSION
    }


@app.get("/health")
def health():
    """Health check endpoint for Azure Container Instance monitoring.

    Used by the Dockerfile HEALTHCHECK instruction to verify
    the container is responsive and ready to serve requests.

    Returns:
        JSON with status 'ok' and current API version.
    """
    return {"status": "ok", "version": APP_VERSION}


@app.post("/predict", response_model=PredictionResponse)
def predict_sales(data: SalesPrediction):
    """Generate a sales prediction for a given product.

    Applies a stochastic model that estimates future sales based on
    the provided base sales figure, with a random growth factor
    between -10% and +30%.

    Args:
        data: SalesPrediction object containing product name,
              base sales figure, and target month.

    Returns:
        PredictionResponse with predicted sales and confidence score.

    Example request body:
        {
            "product": "ProductoA",
            "base_sales": 1000.0,
            "month": 5
        }
    """
    inicio = time.time()

    # Apply stochastic growth factor: uniform distribution [-10%, +30%]
    prediction = round(data.base_sales * (1 + random.uniform(-0.1, 0.3)), 2)
    confidence = round(random.uniform(0.75, 0.95), 2)
    nivel = _nivel_confianza(confidence)

    # Calculate response latency for observability
    latencia_ms = round((time.time() - inicio) * 1000, 2)

    # Structured log for Azure Monitor / CloudWatch ingestion
    logger.info(
        "Prediction: product=%s predicted=%.2f confidence=%.2f level=%s latency=%.1fms",
        data.product, prediction, confidence, nivel, latencia_ms
    )

    return PredictionResponse(
        product=data.product,
        predicted_sales=prediction,
        confidence=confidence
    )