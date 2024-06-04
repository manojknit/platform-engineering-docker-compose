import pytest
from fastapi.testclient import TestClient
from server.api.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running"}
