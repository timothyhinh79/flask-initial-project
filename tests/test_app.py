import pytest
import json
from api.models import Crime
from api import get_db, create_app
from api.orm import build_record, save_record, drop_records

@pytest.fixture
def app():
    flask_app = create_app(user = 'postgres', password = 'postgres', database = 'crimes_test')

    with flask_app.app_context():
        conn, cursor = get_db(user = 'postgres', password = 'postgres', database = 'crimes_test')
        drop_records(conn, cursor, 'crimes')
        build_sample_records(conn, cursor)
        conn.commit()

    yield flask_app

    with flask_app.app_context():
        drop_records(conn, cursor, 'crimes')
        conn.commit()

def build_sample_records(conn, cursor):
    crime_one = Crime(id = 1)
    crime_two = Crime(id = 2)
    save_record(conn, cursor, crime_one, 'crimes')
    save_record(conn, cursor, crime_two, 'crimes')

@pytest.fixture
def client(app):
    return app.test_client()

def test_crimes_route(app, client):
    json_response = json.loads(client.get('/crimes').data)
    assert len(json_response) == 2
    assert json_response[0]['id'] == 1
    assert json_response[1]['id'] == 2

def test_show_crime(app, client):
    json_response = json.loads(client.get('/crimes/1').data)
    assert json_response['id'] == 1

    json_response = json.loads(client.get('/crimes/2').data)
    assert json_response['id'] == 2




        


        


