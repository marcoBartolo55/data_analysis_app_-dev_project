from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, '../templates')
STATIC_DIR = os.path.join(BASE_DIR, '../static')

app = FastAPI()
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Rutas de la aplicación
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/financial")
def financial(request: Request):
    return templates.TemplateResponse("financial.html", {"request": request})

@app.get("/scraper")
def scraper(request: Request):
    return templates.TemplateResponse("scaper.html", {"request": request})

# API: Películas (JSON)
@app.get("/api/peliculas")
def api_peliculas():
    data_path = os.path.join(BASE_DIR, '../spyder/data/peliculas.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except FileNotFoundError:
        return JSONResponse(content={"error": "peliculas.json no encontrado"}, status_code=404)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
