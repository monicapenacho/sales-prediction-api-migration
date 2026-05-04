"""
Tests for ABC Analytics Sales Prediction API.

Covers all endpoints: root, health check, and sales prediction.
Uses FastAPI TestClient for in-process HTTP testing without
requiring a running server.

Author: Juan Manuel Campos Enrique / Mónica Penacho
"""

# import pytest
from fastapi.testclient import TestClient
from app.main import app

# Initialize test client — no server required
client = TestClient(app)

# Sample valid prediction request payload
SAMPLE_PREDICTION_REQUEST = {
    "product": "ProductoA",
    "base_sales": 1000.0,
    "month": 5
}


def test_root_returns_200():
    """Root endpoint should return HTTP 200 and a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check_returns_ok():
    """Health endpoint should return status 'ok' for container monitoring."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_returns_200_with_valid_data():
    """Predict endpoint should return HTTP 200 with a valid request body."""
    response = client.post("/predict", json=SAMPLE_PREDICTION_REQUEST)
    assert response.status_code == 200


def test_predict_response_contains_expected_fields():
    """Predict response should contain product, predicted_sales and confidence."""
    response = client.post("/predict", json=SAMPLE_PREDICTION_REQUEST)
    data = response.json()
    assert "predicted_sales" in data
    assert "confidence" in data
    assert "product" in data


def test_predict_invalid_schema_returns_422():
    """Predict endpoint should return HTTP 422 when request body is invalid."""
    response = client.post("/predict", json={"product": "A", "base_sales": "not_a_number"})
    assert response.status_code == 422


def test_predict_confidence_between_0_and_1():
    """Confidence score should always be a float between 0 and 1."""
    response = client.post("/predict", json=SAMPLE_PREDICTION_REQUEST)
    confidence = response.json()["confidence"]
    assert 0.0 <= confidence <= 1.0


def test_predict_sales_greater_than_zero():
    """Predicted sales should always be a positive number."""
    response = client.post("/predict", json=SAMPLE_PREDICTION_REQUEST)
    predicted = response.json()["predicted_sales"]
    assert predicted > 0