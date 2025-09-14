# File: /janmarg/janmarg/backend/tests/test_synthetic.py

import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_synthetic_detector_valid_image():
    with open("tests/test_images/valid_image.jpg", "rb") as image_file:
        response = client.post("/api/synthetic", files={"file": image_file})
    assert response.status_code == 200
    assert "is_synthetic" in response.json()
    assert "confidence" in response.json()
    assert "artifact_note" in response.json()

def test_synthetic_detector_invalid_image():
    with open("tests/test_images/invalid_image.txt", "rb") as image_file:
        response = client.post("/api/synthetic", files={"file": image_file})
    assert response.status_code == 400
    assert "detail" in response.json()

def test_synthetic_detector_no_image():
    response = client.post("/api/synthetic")
    assert response.status_code == 400
    assert "detail" in response.json()