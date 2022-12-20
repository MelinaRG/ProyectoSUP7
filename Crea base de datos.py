from peewee import PostgresqlDatabase, Model, CharField, ForeignKeyField, IntegerField,IntegrityError


DBNAME = "sup_db"
DBUSER = "su_admin"
DBKEY = "pgsup07"
DBHOST = "tcp-mo5.mogenius.io"
DBPORT = 43829


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


db.connect()
"""db.create_tables([Usuario])
#db.drop_tables([Usuario])
print(db.get_tables())"""

def create_user(nombre,apellido,edad,email):
    try:
        with db.atomic():
            Usuario.create(
                nombre = 'batman',
                apellido = 'betmen',
                edad = 99,
                email = 'batman@hola.com',
            )
    except IntegrityError:
        print(f'That email is already taken')
email = 'carlos12@gmail.com'
data = Usuario.select().where(Usuario.email == email)
print(data[0].nombre,data[0].apellido,data[0].edad,data[0].email)
#db.drop_tables([Testerino,Testerino_rel])
#print(db.get_tables())"""
db.close()