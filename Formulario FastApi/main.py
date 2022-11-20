import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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
async def post_form(request: Request):
    if Request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        nacionalidad = request.form['nacionalidad']
        preferencia = request.form['preferencia']
        conocimiento = request.form['conocimiento']
    return "Gracias por responder"           

if __name__ == '__main__':
    uvicorn.run(app)