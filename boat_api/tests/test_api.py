import pytest
from boat_api.app import FlaskAppFactory
from boat_api.routes import add_routes
from boat_api.utils.config import load_config

load_config()

@pytest.fixture()
def app():
    factory = FlaskAppFactory()
    app = factory.create_app("development")
    add_routes(app)
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_stations(client):
    response = client.get("/api/v1/stations/100/59.40225,18.35317")
    assert b"59.40225" in response.data
