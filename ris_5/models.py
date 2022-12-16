from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Float,
    create_engine,
)
from sqlalchemy.orm import registry, sessionmaker
from sqlalchemy.ext.horizontal_shard import ShardedSession

from ris_5 import settings


mapper_registry = registry()
postgres_mater_engine = create_engine(settings.POSTGRES_MASTER_URI)
postgres_slave_engine = create_engine(settings.POSTGRES_SLAVE_URI)
mariadb_first_master_engine = create_engine(settings.MARIADB_FIRST_MASTER_URI)
mariadb_second_master_engine = create_engine(settings.MARIADB_SECOND_MASTER_URI)
engines = {
    settings.POSTGRES_MASTER_LABEL: postgres_mater_engine,
    settings.POSTGRES_SLAVE_LABEL: postgres_slave_engine,
    settings.MARIADB_FIRST_MASTER_LABEL: mariadb_first_master_engine,
    settings.MARIADB_SECOND_MASTER_LABEL: mariadb_second_master_engine,
}


def shard_chooser(*args, **kwargs):
    pass


def id_chooser(*args, **kwargs):
    pass


def execute_chooser(context):
    return [context.execution_options['shard_id']]


session_factory = sessionmaker(
    class_=ShardedSession,
    future=True,
    shards=engines,
    shard_chooser=shard_chooser,
    id_chooser=id_chooser,
    execute_chooser=execute_chooser,
)


dataset_table = Table(
    'dataset',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True),
    Column('sex', String(1), nullable=False),
    Column('length', Float, nullable=False),
    Column('diameter', Float, nullable=False),
    Column('height', Float, nullable=False),
    Column('weight_1', Float, nullable=False),
    Column('weight_2', Float, nullable=False),
    Column('weight_3', Float, nullable=False),
    Column('weight_4', Float, nullable=False),
    Column('target', Integer, nullable=False),
)
