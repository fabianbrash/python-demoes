import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

hello_msg = {
    'message': 'Hello World'
}

books = [
    {
     'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'
     },
    {
     'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'
     },
    {
     'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'
     }
]

@app.route('/', methods=['GET'])

def home():
    return '''<h1>Welcome to my API</h1>
    <p>API's in Python are cool</p>'''

@app.route('/api/v1/hello', methods=['GET'])

def hello():
    return jsonify(hello_msg)

@app.route('/api/v1/books/all', methods=['GET'])

def api_all():
    return jsonify(books)

app.run()


