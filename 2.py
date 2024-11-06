!pip install ipython-sql
%load_ext sql
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
SELECT departure_airport, arrival_airport
FROM Flights 
JOIN Ticket_flights USING(flight_id)
JOIN Tickets t USING(ticket_no)
Where t.passenger_name='ELLA DMITRIEVA'

%%sql $CONNECT_DATA

SELECT 
    f.departure_airport, 
    a1.city AS departure_city, 
    f.arrival_airport, 
    a2.city AS arrival_city
FROM Flights f
JOIN Ticket_flights tf ON f.flight_id = tf.flight_id
JOIN Tickets t ON tf.ticket_no = t.ticket_no
JOIN Airports a1 ON f.departure_airport = a1.airport_code
JOIN Airports a2 ON f.arrival_airport = a2.airport_code
WHERE t.passenger_name = 'ELLA DMITRIEVA';
