from flask import abort, request, current_app
from flask_restx import Namespace, Resource, fields
import requests, validators, re

api = Namespace('words', 'Words related operations')

word_model = api.model('Word', {
    'word': fields.String,
    'counter': fields.Integer
})

counter_model = api.model('Counter', {
    'type': fields.String,
    'data': fields.String
})


class Word:
    def __init__(self, word, counter):
        self.word = word
        self.counter = counter


class Counter:
    def __init__(self, type, counter):
        self.type = type
        self.counter = counter


@api.route('/stats/<word>')
class WordStats(Resource):
    @api.marshal_with(word_model, code=200, description='Word count retrieved')
    def get(self, word):
        if word is None:
            abort(400, custom='Key is None')
        stats = query(word)
        return Word(word, stats)


@api.route('/counter', methods=['POST'])
class WordCounter(Resource):
    @api.response(code=200, description='Text processed')
    @api.expect(counter_model, validation=True)
    def post(self):
        content = request.get_json()
        if content['type'] == 'string':
            persistence = current_app.extensions['persistence'].open()
            process_string(content['data'], persistence)
            current_app.extensions['persistence'].write(persistence)

        elif content['type'] == 'file':
            persistence = current_app.extensions['persistence'].open()
            with open(content['data']) as fh:
                for line in fh:
                    process_string(line, persistence)
            current_app.extensions['persistence'].write(persistence)

        elif content['type'] == 'url':
            persistence = current_app.extensions['persistence'].open()
            for line in make_request(content['data']):
                if line:
                    decoded_line = line.decode('utf-8')
                    process_string(decoded_line, persistence)
            current_app.extensions['persistence'].write(persistence)

        else:
            abort(400, custom='Malformed request')


def make_request(url):
    if not validators.url(url):
        abort(400, custom='Invalid url')
    try:
        response = requests.get(url, stream=True)
        return response.iter_lines()
    except Exception as e:
        abort(500, f'Internal error: {e}')


def process_string(data, persistence):
    for word in clean_text(data).split():
        try:
            persistence[word] += 1
        except KeyError:
            persistence[word] = 1


def query(key):
    persistence = current_app.extensions['persistence'].open()
    if clean_text(key) in persistence:
        return persistence[key]
    return 0


def clean_text(data):
    clean = data.lower()
    return re.sub(r'[^a-z ]', '', clean)
