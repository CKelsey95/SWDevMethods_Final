import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200

def test_room_route(client):
    with client.session_transaction() as sess:
        sess['room'] = 'test_room'
        sess['name'] = 'test_user'
    response = client.get('/room')
    assert response.status_code == 302

def test_message_event(client):
    response = client.post('/', data={'name': 'test_user', 'code': 'test_room'})
    assert response.status_code == 200
    response = client.get('/room', follow_redirects=True)
    assert response.status_code == 200

def test_connect_event(client):
    with client.session_transaction() as sess:
        sess['room'] = 'test_room'
        sess['name'] = 'test_user'
    client.get('/room')
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200

def test_disconnect_event(client):
    with client.session_transaction() as sess:
        sess['room'] = 'test_room'
        sess['name'] = 'test_user'
    client.get('/room')
    response = client.get('/', follow_redirects=True)
    assert response.status_code == 200
