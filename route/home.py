from flask import Blueprint

home = Blueprint('home', __name__, template_folder='templates')

from src.controllers import home_controller