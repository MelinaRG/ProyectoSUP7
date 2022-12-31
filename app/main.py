import uvicorn
from fastapi import FastAPI, Request, Form, Depends, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db_postgres import conn 
from db_postgres import create_user
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager 
from fastapi_login.exceptions import InvalidCredentialsException 
from datetime import timedelta

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SECRET = "c67b468dd8b0055b207c639cc268ab63632427e47d3818eb"

manager = LoginManager(SECRET,'/auth/login',use_cookie=True)
manager.cookie_name = "some-name"


@manager.user_loader()
def load_user(username:str):
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ta WHERE email=%s", (username,))
    
    result = cursor.fetchone()

    if result:
        user_dict = {
            "nombre": result[1],
            "apellido": result[2],
            "email": result[3],
            "pw": result[4],
            "id_sup": result[5],
        }
    
        return user_dict
    else:
        return None

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

@app.post("/auth/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    user = load_user(username)
    if not user:
        raise InvalidCredentialsException
    elif password != user['pw']:
        raise InvalidCredentialsException
    access_token = manager.create_access_token(
        data={"sub":username},
        expires=timedelta(hours=1)
    )
    resp = RedirectResponse(url="/juegos",status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp


@app.get("/juegos", response_class=HTMLResponse, _=Depends(manager))
async def juegos(request: Request):
    return templates.TemplateResponse("juegos.html",{
        "request": request
        })

@app.get("/temas", response_class=HTMLResponse, _=Depends(manager))
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


