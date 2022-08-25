from api import Crime, build_record, save_record, drop_records
import psycopg2

### testing


crime_one = Crime(id = 1)

conn = psycopg2.connect(database = 'crimes_test', user = 'postgres', password = 'postgres')
cursor = conn.cursor()
drop_records(conn, cursor, 'crimes')
#save_record(conn, cursor, crime_one, 'crimes')
