from app.constants import *
from app.model.AuthModel import AuthModel
from app.services.helper import successResponse
from http import HTTPStatus

class AuthController(AuthModel):
    
    def __init__(self):
        super().__init__()
    
    def login(self):
        result = AuthModel().user_login()
        return successResponse(SUCCESS_MSG, result, HTTPStatus.OK)