from flask import Blueprint

# from ..app.controllers.views import views
# from ..app.main.errors import errors

home = Blueprint('home', __name__, template_folder='templates')

from src.controllers import home_controller