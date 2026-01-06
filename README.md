# Proyecto -- Evaluador de Películas

```shell
#* Depreceated Flask
#* Forma de iniciar la aplicación en Unix (recomendado desde la raíz del proyecto):
python3 -m venv .venv                 # Crear entorno virtual (solo la primera vez)
source .venv/bin/activate             # Activar el entorno
python -m pip install --upgrade pip   # Actualizar pip
python -m pip install -r requirements.txt  # Instalar dependencias del proyecto

# Proyecto — Data Analysis Cinema

## Iniciar la aplicación (FastAPI)

Requisitos: Python 3.12+, `fastapi`, `uvicorn`, `jinja2` (incluidos en `requirements.txt`).
```

```bash
# Crear y activar entorno virtual (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Arrancar el servidor de desarrollo (desde la raíz del repo)
uvicorn app.app:app --reload

# Opcional: puerto específico
uvicorn app.app:app --reload --port 8000
```

Windows (PowerShell):
```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn app.app:app --reload
```

- La app monta estáticos en `/static` y plantillas en `templates`.
- Endpoints principales: `/`, `/financial`, `/scraper`, `/api/peliculas`.

## Deprecated: inicio con Flask

El arranque de la aplicación con Flask ha sido deprecado y no se mantiene. Si necesitas replicar el comportamiento anterior, usa FastAPI como se indica arriba.

Comandos históricos (no recomendados):
```bash
flask --app app/app.py run --debug
python3 app/app.py
```

## Scrapy (TMDB) — Organización y uso

Este directorio contiene el proyecto Scrapy para extraer datos de TMDB.

### Estructura recomendada
- `scrapy.cfg`: Configuración del proyecto Scrapy.
- `mdb_project/`: Código del proyecto (spiders, settings, items, pipelines).
  - `spiders/tmdb.py`: Spider principal que consume la API de TMDB.
  - `settings.py`: Configuración (salidas y logs).
- `data/`: Salidas JSON generadas automáticamente por los crawls.
- `logs/`: Archivos de log de las ejecuciones de Scrapy.

### Cómo ejecutar

```bash
cd spyder
export TMDB_API_KEY="tu_api_key"
scrapy crawl tmdb
```

- La salida se guardará automáticamente en `spyder/data/` con nombre dinámico: `tmdb-YYYYMMDD_HHMMSS.json`.
- El log se registra en `spyder/logs/scrapy.log`.

> Consejo: para actualizar `requirements.txt` con las dependencias actuales del entorno, puedes usar `pip freeze > requirements.txt`.