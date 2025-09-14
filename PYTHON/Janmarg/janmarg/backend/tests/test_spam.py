import pytest
from fastapi.testclient import TestClient
from janmarg.backend.api.main import app

client = TestClient(app)

def test_spam_classifier():
    # Test case for spam classification
    response = client.post("/spam", json={"text": "Congratulations! You've won a lottery!"})
    assert response.status_code == 200
    assert "spam" in response.json()["classification"]

    response = client.post("/spam", json={"text": "Hello, how are you?"})
    assert response.status_code == 200
    assert "not spam" in response.json()["classification"]

def test_invalid_input():
    # Test case for invalid input
    response = client.post("/spam", json={"text": ""})
    assert response.status_code == 400
    assert "detail" in response.json()  # Expecting a validation error

def test_spam_classifier_edge_cases():
    # Test case for edge cases
    response = client.post("/spam", json={"text": "Win a free iPhone!"})
    assert response.status_code == 200
    assert "spam" in response.json()["classification"]

    response = client.post("/spam", json={"text": "This is a test message."})
    assert response.status_code == 200
    assert "not spam" in response.json()["classification"]