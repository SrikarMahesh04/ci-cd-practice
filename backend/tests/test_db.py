from sqlalchemy import text
from app.db import engine


def test_database_connection():
    with engine().connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        assert result == 1


def test_migrations_applied():
    with engine().connect() as conn:
        revision = conn.execute(text("SELECT version_num FROM alembic_version")).scalar()
        assert revision == "0007"

