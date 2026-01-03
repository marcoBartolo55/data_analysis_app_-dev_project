# Proyecto -- Evaluador de Películas

```shell
#* Forma de iniciar la aplicación en Unix (recomendado desde la raíz del proyecto):
python3 -m venv .venv                 # Crear entorno virtual (solo la primera vez)
source .venv/bin/activate             # Activar el entorno
python -m pip install --upgrade pip   # Actualizar pip
python -m pip install -r requirements.txt  # Instalar dependencias del proyecto

# Levantar la app Flask
flask --app app/app.py run --debug    
cd ./app /


# Alternativa (sin CLI de Flask):
python3 app/app.py
```
Notas:
- Si ejecutas `flask run` desde otro directorio (p. ej. `app/modules`), usa siempre `--app app/app.py` o muévete a la raíz donde se inicia el aplicación `app.py`.
- El error de salida `2` suele indicar que Flask no encuentra `FLASK_APP`/`--app`. Usa las rutas anteriores.

```shell
#* Formas de iniciar la aplicación en Windows (no se si funcionan apropiadamente):
py -3 -m venv .venv                  # Crear entorno virtual (solo la primera vez)
.venv\\Scripts\\activate            # Activar el entorno
python -m pip install --upgrade pip  # Actualizar pip
python -m pip install -r requirements.txt  # Instalar dependencias del proyecto
flask --app app\app.py run           # Levantar la app Flask
```

Para contar con todas las librerías para el funcionamiento correcto del proyecto, ejecutar el siguiente comnado en la línea de la terminal:
```shell
pip install -r requirements.txt
```


# Scrapy (TMDB) — Organización y uso

Este directorio contiene tu proyecto Scrapy para extraer datos de TMDB.

## Estructura recomendada
- `scrapy.cfg`: Configuración del proyecto Scrapy.
- `mdb_project/`: Código del proyecto (spiders, settings, items, pipelines).
  - `spiders/tmdb.py`: Spider principal que consume la API de TMDB.
  - `settings.py`: Configuración (salidas y logs).
- `data/`: Salidas JSON generadas automáticamente por los crawls.
- `logs/`: Archivos de log de las ejecuciones de Scrapy.


## Cómo ejecutar

```bash
cd spyder
export TMDB_API_KEY="tu_api_key"
scrapy crawl tmdb
```

- La salida se guardará automáticamente en `spyder/data/` con nombre dinámico: `tmdb-YYYYMMDD_HHMMSS.json`.
- El log se registra en `spyder/logs/scrapy.log`.

## Configuración clave

- En `settings.py`, `FEEDS` usa `%(name)s` y `%(time)s` para evitar sobreescritura y mantener histórico de ejecuciones.
- El spider lee `TMDB_API_KEY` desde variables de entorno.
- Puedes ajustar el número de páginas en `TmdbSpider.max_pages` dentro de `spiders/tmdb.py`.

## Integración con la app Flask

- Desde tu app, lee los archivos JSON de `spyder/data/` según necesites.
- Si quieres un nombre fijo, cambia `FEEDS` a un archivo estático y pon `overwrite: True`.

## Buenas prácticas

- Mantén `data/` y `logs/` fuera de control de versiones (`.gitignore`).
- Usa ambientes virtuales y variables de entorno para credenciales.
- Versiona solo el código del spider y configuraciones, no los resultados.

[pip freeze > requirements.txt --> Formas de guardar los requerimientos con los que cuenta la aplicación]:#