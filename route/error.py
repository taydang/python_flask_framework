from flask import Blueprint

error = Blueprint('error', __name__, template_folder='templates/errors/')

from src.controllers import error_controller