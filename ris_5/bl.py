import csv

from sqlalchemy import insert, select, func
from sqlalchemy.ext.horizontal_shard import ShardedSession

from ris_5.models import dataset_table

DATASET_PATH = './data/dataset.csv'
BATCH_SIZE = 1000


def load_dataset(db_label: str, session: ShardedSession) -> None:
    base_insert_query = insert(dataset_table)
    with open(DATASET_PATH, newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        insert_values = []
        for row in reader:
            insert_values.append(
                {
                    'sex': row['sex'],
                    'length': float(row['length']),
                    'diameter': float(row['diameter']),
                    'height': float(row['height']),
                    'weight_1': float(row['weight_1']),
                    'weight_2': float(row['weight_2']),
                    'weight_3': float(row['weight_3']),
                    'weight_4': float(row['weight_4']),
                    'target': int(row['target']),
                },
            )

            if len(insert_values) == BATCH_SIZE:
                session.execute(
                    base_insert_query.values(insert_values),
                    execution_options={'shard_id': db_label},
                )
                session.commit()
                insert_values = []

        if insert_values:
            session.execute(
                base_insert_query.values(insert_values),
                execution_options={'shard_id': db_label},
            )
            session.commit()


def count_dataset_items(db_label: str, session: ShardedSession) -> int:
    result = session.execute(
        select(func.count()).select_from(dataset_table),
        execution_options={'shard_id': db_label},
    )
    return result.scalar_one()


def count_dataset_by_sex(db_label: str, session: ShardedSession) -> dict[str, int]:
    query = (
        select(
            [
                dataset_table.c.sex,
                func.count(),
            ]
        )
        .group_by(dataset_table.c.sex)
    )
    result = session.execute(query, execution_options={'shard_id': db_label})
    return {sex: count for sex, count in result.all()}
