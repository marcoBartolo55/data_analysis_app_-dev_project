from flask import Flask

# Nombra la instancia como 'app' (es la convención por defecto)
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Mundo!"

# Opcional: Esto no es necesario al usar 'flask run', pero no molesta
if __name__ == '__main__':
    app.run(debug=True)