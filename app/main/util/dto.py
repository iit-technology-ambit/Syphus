# Data Transfer Object- Responsible for carrying data between processes
from flask_restplus import Namespace, fields


class AuthDto:
    api = Namespace('auth', description='Authentication Related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='Login Email'),
        'password': fields.String(required=True, description='Login Password'),
        'remember' : fields.String(description = 'Stay Logged In'), 
    })


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })
