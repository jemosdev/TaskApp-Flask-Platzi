# se declara el modulo auth como blueprint y se establece la url que usara dentro de la app
from flask import Blueprint

auth= Blueprint('auth', __name__, url_prefix= '/auth')

from . import views
