import pytest
import sys
import os

# Adicionar o diretório src ao path do Python
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_hello_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert 'message' in response.json