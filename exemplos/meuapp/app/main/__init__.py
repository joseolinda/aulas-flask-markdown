from flask import Blueprint

main_bp = Blueprint('main', __name__)
main_bp.template_folder = 'templates'

from . import views