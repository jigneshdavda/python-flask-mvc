from flask import Blueprint
from app.controller.admin.AuthController import AuthController

admin_api = Blueprint('admin_api', __name__,url_prefix='/api/admin')

admin_api.add_url_rule('/login',view_func=AuthController().login, methods=['POST'])