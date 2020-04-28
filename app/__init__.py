import os
from flask import Flask
from .api import api
from .persistence.persistence import Persistence

persistence = Persistence()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object('config.Config')
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    with app.app_context():
        api.init_app(app)
        persistence.init_app(app)

        return app
