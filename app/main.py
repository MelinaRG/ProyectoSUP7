import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scripts.db_postgres import create_user
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.get("/login", response_class=HTMLResponse)
async def loginx(request: Request):
    return templates.TemplateResponse("login.html",{
        "request": request
        })

@app.get("/juegos", response_class=HTMLResponse)
async def juegos(request: Request):
    return templates.TemplateResponse("juegos.html",{
        "request": request
        })

@app.get("/temas", response_class=HTMLResponse)
async def temas(request: Request):
    return templates.TemplateResponse("temas.html",{
        "request": request
        })

@app.post("/add_contact", response_class=HTMLResponse)
async def post_form (request: Request, 
            grupo_sup: int = Form(...),
            nombre: str = Form(...),
            apellido: str = Form(...),
            edad: int = Form(...),
            email: str = Form(...),
            nacionalidad: str = Form(...),
            pais_residencia: str = Form(...),
            ocupacion: str = Form(...),
            dispositivo: str = Form(...),
            mic_y_cam: str = Form(...),
            funcion_sup: str = Form(...),
            gustos_sup: str = Form(...),):

            lista = []

            lista.append(grupo_sup)
            lista.append(nombre)
            lista.append(apellido)
            lista.append(edad)
            lista.append(email)
            lista.append(nacionalidad)
            lista.append(pais_residencia)
            lista.append(ocupacion)
            lista.append(dispositivo)
            lista.append(mic_y_cam)
            lista.append(funcion_sup)
            lista.append(gustos_sup)

            create_user(lista)

            return 'Gracias por responder'

if __name__ == '__main__':
    uvicorn.run(app, port=80)


import os
import psycopg2

# Crea la conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    DBNAME = os.environ["DBNAME"],
    DBUSER = os.environ["DBUSER"],
    DBKEY = os.environ["DBKEY"],
    DBHOST = os.environ["DBHOST"],
    DBPORT = os.environ["DBPORT"]
)

# Define el modelo de datos para la información de inicio de sesión
class LoginData(BaseModel):
    username: str
    password: int

# Crea una ruta para manejar las solicitudes de inicio de sesión
@app.post("/login")
async def login(data: LoginData):
    # Obtiene los datos de inicio de sesión de la solicitud
    username = data.username
    password = data.password

    # Realiza una consulta SELECT para obtener la información de usuario de la tabla
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ta WHERE email = %s', (username,))
    result = cursor.fetchone()

    # Si no se encontró un usuario con ese nombre, devuelve un código de estado HTTP 401 y un mensaje de error
    if result is None:
        return {"error": "Invalid username or password"}, 401

    # Compara la contraseña hasheada almacenada con la contraseña enviada por el cliente
    if password == result[4]:
        # Si la contraseña es correcta, devuelve un código de estado HTTP 200 y un mensaje de éxito
        return {"message": "Login successful"}
    else:
        # Si la contraseña es incorrecta, devuelve un código de estado HTTP 401 y un mensaje de error
        return {"error": "Invalid username or password"}, 401