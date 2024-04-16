from app import app as flask_app
import pytest
import json

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home(app, client):
    res = client.get('/')
    assert res.status_code == 200
    
def test_room(app, client):
   res = client.get('/room')
   assert res.status_code == 200 