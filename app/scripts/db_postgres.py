import os
import psycopg2, psycopg2.extras


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
#NOTE COPIERINO
def get_asistencia(id_sup = 0): #NOTE sacar hardcode
    data = id_sup #NOTE sacar hardcode
    engine = conn
    cur = engine.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('SELECT * FROM ta')
    data1 = cur.fetchall()
    data = {}
    for e,row in enumerate(data1):
        data[e] = dict(row)
    cur.close()
    return data

#NOTE END COPIERINO

