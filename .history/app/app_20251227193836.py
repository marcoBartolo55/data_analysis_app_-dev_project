from flask import Flask, render_template
import os

#* Forma de iniciar la aplicación en Unix:
'''
python3 -m venv .venv                 # Crear entorno virtual (solo la primera vez)
source .venv/bin/activate             # Activar el entorno
python -m pip install --upgrade pip   # Actualizar pip
python -m pip install -r requirements.txt  # Instalar dependencias del proyecto
FLASK_APP=app.py flask run            # Levantar la app Flask
'''

#* Formas de iniciar la aplicación en Windows (no se si funcionan apropiadamente):
'''
py -3 -m venv .venv                  # Crear entorno virtual (solo la primera vez)
.venv\\Scripts\\activate            # Activar el entorno
python -m pip install --upgrade pip  # Actualizar pip
python -m pip install -r requirements.txt  # Instalar dependencias del proyecto
set FLASK_APP=app.py && flask run    # Levantar la app Flask
'''

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static')
           )

#* Routeo de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/financial')
def financial():
    return render_template('financial.html')

@app.route('/successful')
def successful():
    return render_template('succesful.html')

@app.route('/scraper')
def scraper():
    return render_template('scaper.html')

#* Métodos operativos de la aplicación


#* Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)