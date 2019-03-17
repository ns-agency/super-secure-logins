import os
import sys

from flask import Flask
from sqlalchemy import create_engine


class ConfigClass(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'A_DEFAULT_SECRET_KEY_OH_NO')
    TITLE = "NSA Admin Portal"
    NAVBAR = []
    LOGIN_FORM = True
    THEME = "flatly"
    STATIC_URL_PATH = "/static"

    try:
        FLAG = os.environ['FLAG']
        FLAG_SECRET = os.environ['FLAG_SECRET']
        DB_CONNECTION_STRING = os.environ['DB_CONNECTION_STRING']
    except KeyError as e:
        if "pytest" not in sys.modules:
            raise e

        FLAG = "IF_I_SEE_THIS_THIS_AINT_PATCHED"
        FLAG_SECRET = "lolno"


def register_models(app):
    from . import models


def register_blueprints(app):
    from .basic import app as basic_bp
    app.register_blueprint(basic_bp)


def create_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + '.ConfigClass')

    register_models(app)
    register_blueprints(app)

    # setup our database connection
    if 'DB_CONNECTION_STRING' in app.config:
        app.db = create_engine(app.config['DB_CONNECTION_STRING'])

    return app
