# endpoint for login/logout
# endpoint for user operations
from flask import request
from flask_restplus import Resource

from ..util.dto import UserDto

# Import All API Endpoints Needed for user
# from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user


