from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='templates/auth/', url_prefix='/auth')

from src.controllers import auth_controller