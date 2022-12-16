import pytest

from ris_5.models import (
    mapper_registry,
    session_factory,
    postgres_mater_engine,
    mariadb_first_master_engine,
)

from sqlalchemy.ext.horizontal_shard import ShardedSession


@pytest.fixture
def db_session() -> ShardedSession:
    postgres_mater_conn = postgres_mater_engine.connect()
    mariadb_first_master_conn = mariadb_first_master_engine.connect()

    mapper_registry.metadata.create_all(postgres_mater_conn)
    mapper_registry.metadata.create_all(mariadb_first_master_conn)

    with session_factory() as session:
        try:
            yield session
        except:
            session.rollback()
        else:
            session.commit()

    mapper_registry.metadata.drop_all(postgres_mater_conn)
    mapper_registry.metadata.drop_all(mariadb_first_master_conn)

    postgres_mater_conn.close()
    mariadb_first_master_conn.close()
