from tests.utils.docker_utils import start_db_container
from tests.utils.database_utils import migrate_to_db
import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="session", autouse=True)
def db_session():
    container = start_db_container()

    engine = create_engine(os.getenv("TEST_DATABASE_URL"))

    with engine.begin() as connection:
        migrate_to_db("migration", "alembic.ini", connection)
    

    SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
    
    yield SessionLocal

    container.stop()
    container.remove()
    engine.dispose()