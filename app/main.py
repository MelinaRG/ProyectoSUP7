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
        "request": request,
        "message": "Hola gente, por favor completa tus datos"
    })

@app.post("/add_contact", response_class=HTMLResponse)
async def post_form (request: Request, nombre: str = Form(...),
            apellido: str = Form(...),
            edad: int = Form(...),
            email: str = Form(...),):
            
            lista = []

            lista.append(nombre)
            lista.append(apellido)
            lista.append(edad)
            lista.append(email)

            create_user(lista)

            return 'Gracias por responder'

if __name__ == '__main__':
    uvicorn.run(app, port=80)