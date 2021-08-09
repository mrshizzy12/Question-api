from app.dependency import get_db
from . import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_api_connect():
    response = client.get('/api/question/')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}
    

