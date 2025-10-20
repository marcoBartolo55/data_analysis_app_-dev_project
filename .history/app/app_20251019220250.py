from flask.templating import render_template
from flask import Flask


app = Flask(__name__)

post = []

@app.route('/')
def index():
    return render_template('../templates/index.html')

if __name__ == '__main__':
    app.run(debug=True)