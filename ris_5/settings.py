import os

POSTGRES_MASTER_LABEL = 'postgres_master'
POSTGRES_SLAVE_LABEL = 'postgres_slave'
MARIADB_FIRST_MASTER_LABEL = 'mariadb_first_master'
MARIADB_SECOND_MASTER_LABEL = 'mariadb_second_master'

POSTGRES_MASTER_URI = os.getenv(
    'POSTGRES_MASTER_URI',
    'postgresql://postgres:my_password@postgresql-master:5432/my_database',
)
POSTGRES_SLAVE_URI = os.getenv(
    'POSTGRES_SLAVE_URI',
    'postgresql://postgres:my_password@postgresql-slave:5432/my_database',
)
MARIADB_FIRST_MASTER_URI = os.getenv(
    'MARIADB_FIRST_MASTER_URI',
    'mysql://my_user:my_password@mariadb-galera-0:3306/my_database',
)
MARIADB_SECOND_MASTER_URI = os.getenv(
    'MARIADB_SECOND_MASTER_URI',
    'mysql://my_user:my_password@mariadb-galera-1:3306/my_database',
)
