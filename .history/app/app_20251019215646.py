from flask import Flask


app = Flask(__name__)

post = []

@app.route('/')
def index():
    return '{} posts'.format(len(postt))

if __name__ == '__main__':
    app.run(debug=True)