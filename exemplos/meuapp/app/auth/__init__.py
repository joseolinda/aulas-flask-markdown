from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
auth_bp.template_folder = 'templates'

from . import views
