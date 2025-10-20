from flask import Flask, render_template
import os

# ... (El resto de tu código de configuración)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static')
           )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')
    

if __name__ == '__main__':
    app.run(debug=True)