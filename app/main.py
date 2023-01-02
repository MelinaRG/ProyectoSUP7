import uvicorn
from fastapi import FastAPI, Request, Form, Depends, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from db_postgres import conn 
from fastapi.responses import RedirectResponse,HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login import LoginManager 
from fastapi_login.exceptions import InvalidCredentialsException 
from datetime import timedelta

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

SECRET = "c67b468dd8b0055b207c639cc268ab63632427e47d3818eb"

manager = LoginManager(SECRET,'/auth',use_cookie=True)
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
    cursor.close()
    
    
@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("login.html", {
        "request": request
    })

@app.get("/index", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.post("/auth")
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
    if username == "sup@admin.com" and password == user['pw']:
        resp = RedirectResponse(url="/registro",status_code=status.HTTP_302_FOUND)
    else:
        resp = RedirectResponse(url="/index",status_code=status.HTTP_302_FOUND)
    manager.set_cookie(resp,access_token)
    return resp


@app.get("/juegos", response_class=HTMLResponse)
async def juegos(request: Request, user=Depends(manager)):
    return templates.TemplateResponse("juegos.html",{
        "request": request
        })

@app.get("/temas", response_class=HTMLResponse)
async def temas(request: Request, user=Depends(manager)):
    return templates.TemplateResponse("temas.html",{
        "request": request
        })

@app.get("/form", response_class=HTMLResponse)
async def temas(request: Request):
    return templates.TemplateResponse("form.html",{
        "request": request
        })

@app.get("/datos", response_class=HTMLResponse)
async def temas(request: Request, user=Depends(manager)):
     resp = RedirectResponse(url="https://streamlit-9nb6.onrender.com/",status_code=status.HTTP_302_FOUND)
     return resp

@app.get("/asistencia", response_class=HTMLResponse)
async def temas(request: Request, user=Depends(manager)):
    return templates.TemplateResponse("temas.html",{
        "request": request
        })

@app.get("/registro", response_class=HTMLResponse)
async def temas(request: Request, user=Depends(manager)):
    return templates.TemplateResponse("registro_usuarios.html",{
        "request": request
        })

@app.post("/add_alumno")
async def post_form (request: Request):
    data = await request.form()
    lista = []

    for key in data.keys():
        lista.append(data[key])

    return 'Gracias por responder, sus datos fueron enviados con éxito!'

@app.post("/registro_usuario")
async def post_form (request: Request, user=Depends(manager)):
    data = await request.form()
    lista = []

    for key in data.keys():
        lista.append(data[key])

    resp = RedirectResponse(url="/registro",status_code=status.HTTP_302_FOUND)
    return lista





#FUNCION QUE ME RECONOCE EL ID_SUP DEL TA

def id_user(username:str):
    
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
        
        return result[5]
    else:
        return None





