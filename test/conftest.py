import pytest
import tempfile
from app.persistence.persistence import Persistence

from app import create_app


@pytest.fixture
def client():
    test_config = {
        "TESTING": True,
        "DEBUG": True,
        "SECRET_KEY": 'dev',
        "PERSISTENCE_FILE": tempfile.mktemp()
    }

    app = create_app(test_config)
    persistence = Persistence()
    persistence.init_app(app)

    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
