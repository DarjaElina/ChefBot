# tests/test_chat.py
# This file contains automated tests for our API endpoints.
# Tests help us make sure our backend responds correctly.
# For example, here we test that the /ping endpoint returns "pong".
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI backend!"}
