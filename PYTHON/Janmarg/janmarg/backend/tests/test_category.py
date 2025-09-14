import pytest
from fastapi.testclient import TestClient
from janmarg.backend.api.main import app

client = TestClient(app)

def test_category_classifier():
    # Example image data for testing
    image_data = {
        "image": "data:image/jpeg;base64,<base64_encoded_image>"
    }
    
    response = client.post("/category", json=image_data)
    
    assert response.status_code == 200
    assert "category" in response.json()
    assert "confidence" in response.json()
    assert response.json()["category"] in ["news-photo", "document", "meme", "ad", "screenshot", "portrait", "scene"]  # Check against default categories

def test_category_classifier_invalid_image():
    # Example invalid image data for testing
    invalid_image_data = {
        "image": "not_a_valid_image"
    }
    
    response = client.post("/category", json=invalid_image_data)
    
    assert response.status_code == 422  # Unprocessable Entity for invalid input
    assert "detail" in response.json()  # Check for error details in response