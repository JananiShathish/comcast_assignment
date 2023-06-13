import pytest
from app import app

def client():
    with app.test_client() as client:
        yield client

def test_get_market(client):
    response = client.get('/fetch_updates')
    assert response.status_code == 200
   

def test_get_user_by_id(client):
    response = client.get('/fetch_updates/summary')
    assert response.status_code == 200
            