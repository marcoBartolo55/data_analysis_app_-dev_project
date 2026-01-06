from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os
from typing import Optional

# Pipeline functions
try:
    from scripts.run_pipeline import matrix_correlation, roi_chart, roi_chart_by_genre, scatter_plot
except Exception:
    matrix_correlation = None
    roi_chart = None
    roi_chart_by_genre = None
    scatter_plot = None

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

@app.get("/data_analysis")
def data_analysis(request: Request):
    return templates.TemplateResponse("data_analysis.html", {"request": request})

# Alias para compatibilidad con enlaces existentes
@app.get("/financial", name="financial")
def financial(request: Request):
    return templates.TemplateResponse("data_analysis.html", {"request": request})

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

# Endpoints para ejecutar el pipeline y devolver rutas de imagen
@app.post("/api/financial/matrix_correlation")
def api_matrix_correlation():
    if matrix_correlation is None:
        return JSONResponse(content={"error": "run_pipeline no disponible"}, status_code=500)
    try:
        matrix_correlation()
        return {"image": "/static/images/correlation_matrix.png"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/api/financial/roi_chart")
def api_roi_chart():
    if roi_chart is None:
        return JSONResponse(content={"error": "run_pipeline no disponible"}, status_code=500)
    try:
        roi_chart()
        return {"image": "/static/images/general_roi_chart.png"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/api/financial/roi_chart_by_genre")
def api_roi_chart_by_genre(genre: Optional[str] = None):
    if roi_chart_by_genre is None:
        return JSONResponse(content={"error": "run_pipeline no disponible"}, status_code=500)
    if not genre:
        return JSONResponse(content={"error": "Parámetro 'genre' requerido"}, status_code=400)
    try:
        roi_chart_by_genre(genre)
        return {"image": "/static/images/roi_chart_genre.png", "genre": genre}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/api/financial/scatter")
def api_scatter(x_var: str, y_var: str):
    if scatter_plot is None:
        return JSONResponse(content={"error": "run_pipeline no disponible"}, status_code=500)
    try:
        scatter_plot(x_var, y_var)
        return {"image": "/static/images/scatter_varx_vs_vary.png", "x": x_var, "y": y_var}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
