import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scripts.db_postgres import create_user

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {
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
            print("hola cualquier cosa")
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
            print(lista)
            return 'Gracias por responder'

if __name__ == '__main__':
    uvicorn.run(app, port=80)