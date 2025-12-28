from flask import Flask, render_template
import os

#* Forma de iniciar la aplicación:
'''
python3 -m venv .venv -- Iniciar el entorno, si no esta creado
source venv/bin/activate && python -m pip install --upgrade pip && pip install -r requirements.txt || pip install Flask 
source .venv/bin/activate && python -m flask --app app.app run --debug -- Ejecución de la aplicación
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

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/scraper')
def scraper():
    return render_template('')

#* Métodos operativos de la aplicación


#* Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)