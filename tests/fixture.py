from tests.utils.docker_utils import start_db_container
import pytest


@pytest.fixture(scope="session", autouse=True)
def db_session():
    container = start_db_container()