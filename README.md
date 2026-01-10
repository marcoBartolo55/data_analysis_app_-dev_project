# Proyecto — Data Analysis Cinema

## Iniciar la aplicación (FastAPI)

Requisitos: Python 3.12+, `fastapi`, `uvicorn`, `jinja2` (incluidos en `requirements.txt`).

```bash
# Crear y activar entorno virtual (Linux/macOS)
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

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

Compatibilidad: Scrapy funciona en Windows y Unix (Linux/macOS).

Unix (bash/zsh):
```bash
cd spyder
export TMDB_API_KEY="tu_api_key"
scrapy crawl tmdb
```

Windows (PowerShell):
```powershell
cd spyder
$env:TMDB_API_KEY="tu_api_key"
scrapy crawl tmdb
```

- La salida se guardará automáticamente en [spyder/data](spyder/data) con nombre dinámico: `tmdb-YYYYMMDD_HHMMSS.json`.
- El log se registra en [spyder/logs](spyder/logs).

> Consejo: para actualizar `requirements.txt` con las dependencias actuales del entorno, puedes usar `pip freeze > requirements.txt`.

## Deprecated: inicio con Flask

El arranque de la aplicación con Flask ha sido deprecado y no se mantiene. Si necesitas replicar el comportamiento anterior, usa FastAPI como se indica arriba.

Comandos históricos (no recomendados):
```bash
flask --app app/app.py run --debug
python3 app/app.py
```
