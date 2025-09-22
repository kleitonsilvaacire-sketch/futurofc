from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "FuturoFC API is running!" in response.text

def test_user_me_unauthorized():
    response = client.get("/users/me")
    assert response.status_code == 401
