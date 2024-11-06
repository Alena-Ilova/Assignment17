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

%%sql $CONNECT_DATA
SELECT 
    t.passenger_name,
    (
        SELECT MIN(a.city) 
        FROM airports a 
        JOIN flights f ON a.airport_code = f.arrival_airport 
        JOIN ticket_flights tf ON f.flight_id = tf.flight_id
        WHERE tf.ticket_no = t.ticket_no
    ) AS arrival_city
FROM tickets t
WHERE t.ticket_no = '0005432312164';

%%sql $CONNECT_DATA
SELECT 
    t.passenger_name,
    a.city AS arrival_city
FROM 
    tickets t, ticket_flights tf, flights f, airports a
WHERE 
    t.ticket_no = '0005432312164'
    AND t.ticket_no = tf.ticket_no
    AND tf.flight_id = f.flight_id
    AND f.arrival_airport = a.airport_code;
    
%%sql $CONNECT_DATA
SELECT 
    t.passenger_name,
    a.city AS arrival_city
FROM tickets t
JOIN ticket_flights tf ON t.ticket_no = tf.ticket_no
JOIN flights f ON tf.flight_id = f.flight_id
JOIN airports a ON f.arrival_airport = a.airport_code
WHERE t.ticket_no = '0005432312164';