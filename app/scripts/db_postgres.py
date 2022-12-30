from peewee import Model, CharField, IntegerField, IntegrityError
from fastapi import FastAPI, Request, Form, Depends, HTTPException, status, Request
import os
import psycopg2
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel


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
conn.close()

#Formulario
class sup_db(Model):
    class Meta:
        database = conn

class Usuario(sup_db):
    grupo_sup = IntegerField()
    nombre = CharField()
    apellido = CharField()
    edad = IntegerField()
    email = CharField(primary_key = True)
    nacionalidad = CharField()
    pais_residencia = CharField()
    ocupacion = CharField()
    dispositivo = CharField()
    mic_y_cam = CharField()
    funcion_sup = CharField()
    gustos_sup = CharField()

def create_user(lista):
    conn.connect()
    try:
        with conn.atomic():
            Usuario.create(
                grupo_sup = lista[0],
                nombre = lista[1],
                apellido = lista[2],
                edad = lista[3],
                email = lista[4],
                nacionalidad = lista[5],
                pais_residencia = lista[6],
                ocupacion = lista[7],
                dispositivo = lista[8],
                mic_y_cam = lista[9],
                funcion_sup = lista[10],
                gustos_sup = lista[11]
            )
    except IntegrityError:
        print(f'¡Ese correo ya se encuentra registrado! Por favor, intente nuevamente con un nuevo correo.')
    conn.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    nombre: str
    apellido: str


def fake_decode_token(token):

    cursor = conn.cursor()
    
    cursor.execute("SELECT id_sup FROM ta_test_fede WHERE email =%s", (token,))
    
    result = cursor.fetchone()
    
    cursor.close()
    
    if result:
        return result
    else:
        return None


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
