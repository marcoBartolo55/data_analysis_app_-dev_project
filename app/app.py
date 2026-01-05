from flask import Flask, render_template, jsonify
import json
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static')
           )

# Routeo de la aplicación
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/financial')
def financial():
    return render_template('financial.html')

@app.route('/scraper')
def scraper():
    return render_template('scaper.html')

# API: Películas (JSON)
@app.route('/api/peliculas')
def api_peliculas():
    data_path = os.path.join(BASE_DIR, '../spyder/data/peliculas.json')
    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "peliculas.json no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
    
    
# Funciones para recuperar información de los datos