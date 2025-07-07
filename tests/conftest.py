import pytest
from app import create_app

# Fixture for creating a test app instance
@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
    })

    yield app

# Fixture for providing a test client to simulate HTTP requests
@pytest.fixture
def client(app):
    return app.test_client()
