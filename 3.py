!pip install ipython-sql
!env | grep POST

import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'
CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)

%load_ext sql

%%sql
SELECT COUNT(*) AS total_number_of_seats
FROM seats;

%%sql
SELECT *
FROM seats
ORDER BY seat_no;