from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, IntegerField, IntegrityError
import os

DBNAME = os.environ["DBNAME"]
DBUSER = os.environ["DBUSER"]
DBKEY = os.environ["DBKEY"]
DBHOST = os.environ["DBHOST"]
DBPORT = os.environ["DBPORT"]

db = PostgresqlDatabase(DBNAME,user = DBUSER, password = DBKEY, host = DBHOST, port = DBPORT)
db.close()

class sup_db(Model):
    class Meta:
        database = db

class Usuario(sup_db):
    nombre = CharField()
    apellido = CharField()
    edad = IntegerField()
    email = CharField(primary_key = True)

class Testerino_rel(sup_db):
    input2 = CharField()

def create_user(lista):
    db.connect()
    try:
        with db.atomic():
            Usuario.create(
                nombre = lista[0],
                apellido = lista[1],
                edad = lista[2],
                email = lista[3],
            )
    except IntegrityError:
        print(f'¡Ese correo ya se encuentra registrado! Por favor, intente nuevamente con un nuevo correo.')
    db.close()