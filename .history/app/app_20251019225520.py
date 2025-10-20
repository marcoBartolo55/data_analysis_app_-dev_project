from flask.templating import render_template
from flask import Flask
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, '../templates'),
            static_folder=os.path.join(BASE_DIR, '../static')
           )
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')

if __name__ == '__main__':
    app.run(debug=True)