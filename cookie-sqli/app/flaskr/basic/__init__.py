from flask import Blueprint

app = Blueprint(
    'basic',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/basic')

from . import views

