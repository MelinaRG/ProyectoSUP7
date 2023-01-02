import os
import psycopg2


DBNAME = os.environ["DBNAME"]
DBUSER = os.environ["DBUSER"]
DBKEY = os.environ["DBKEY"]
DBHOST = os.environ["DBHOST"]
DBPORT = os.environ["DBPORT"]

conn = psycopg2.connect(
    host=DBHOST,
    database=DBNAME,
    user=DBUSER,
    password=DBKEY,
    port= DBPORT
)



