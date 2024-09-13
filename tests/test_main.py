from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my API"}

def test_process_text():
    response = client.post("/process-text", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"processed_text": "olleh"}

