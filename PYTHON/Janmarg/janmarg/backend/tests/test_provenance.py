import pytest
from fastapi.testclient import TestClient
from janmarg.backend.api.main import app

client = TestClient(app)

def test_provenance_exif_extraction():
    # Test case for EXIF extraction
    response = client.post("/provenance/extract_exif", json={"image_url": "http://example.com/test_image.jpg"})
    assert response.status_code == 200
    assert "exif_data" in response.json()

def test_provenance_reverse_image_search():
    # Test case for reverse image search
    response = client.post("/provenance/reverse_search", json={"image_url": "http://example.com/test_image.jpg"})
    assert response.status_code == 200
    assert "matches" in response.json()

def test_provenance_check_downloaded_reused():
    # Test case for checking if an image is likely downloaded/re-used
    response = client.post("/provenance/check_reused", json={"image_url": "http://example.com/test_image.jpg"})
    assert response.status_code == 200
    assert "likely_reused" in response.json()