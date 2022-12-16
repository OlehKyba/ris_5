from time import sleep

import pytest
from sqlalchemy.ext.horizontal_shard import ShardedSession

from ris_5.settings import (
    POSTGRES_MASTER_LABEL,
    POSTGRES_SLAVE_LABEL,
    MARIADB_FIRST_MASTER_LABEL,
    MARIADB_SECOND_MASTER_LABEL,
)
from ris_5.bl import load_dataset, count_dataset_items, count_dataset_by_sex


def test_postgresql_master_slave_replication(db_session: ShardedSession):
    load_dataset(POSTGRES_MASTER_LABEL, db_session)
    # Give 5 seconds for async replication synchronization
    sleep(1)

    total_count = count_dataset_items(
        POSTGRES_SLAVE_LABEL, db_session
    )
    sex_counts = count_dataset_by_sex(
        POSTGRES_SLAVE_LABEL, db_session
    )

    assert total_count == 3136
    assert sex_counts == {
        'F': 985,
        'I': 991,
        'M': 1160,
    }


@pytest.mark.parametrize(
    'insert_master,read_master',
    (
        (MARIADB_FIRST_MASTER_LABEL, MARIADB_SECOND_MASTER_LABEL),
        (MARIADB_SECOND_MASTER_LABEL, MARIADB_FIRST_MASTER_LABEL),
    ),
)
def test_mariadb_master_master_replication(
    insert_master: str,
    read_master: str,
    db_session: ShardedSession,
):
    load_dataset(insert_master, db_session)
    # Give 5 seconds for async replication synchronization
    sleep(1)

    total_count = count_dataset_items(
        read_master, db_session
    )
    sex_counts = count_dataset_by_sex(
        read_master, db_session
    )

    assert total_count == 3136
    assert sex_counts == {
        'F': 985,
        'I': 991,
        'M': 1160,
    }
