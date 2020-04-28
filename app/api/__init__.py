from flask_restx import Api
from .words import api as words_api

api = Api(prefix='/api', doc='/explorer')
api.add_namespace(words_api)
