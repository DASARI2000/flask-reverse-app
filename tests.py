import pytest
import json
from app import app, db, StringEntry

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@db:3306/strings_db'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_reverse_string(client):
    response = client.post('/reverse', json={'string': 'hello'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['reversed'] == 'olleh'
    assert data['uppercased'] == 'HELLO'
    assert data['trimmed'] == 'hello'

def test_get_strings(client):
    client.post('/reverse', json={'string': ' hello '})
    response = client.get('/strings')
    data = json.loads(response.data)
    assert len(data) == 1
    assert data[0]['original'] == ' hello '
    assert data[0]['reversed'] == ' olleh'
    assert data[0]['uppercased'] == ' HELLO '
    assert data[0]['trimmed'] == 'hello'
