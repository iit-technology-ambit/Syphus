from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth


def authenticate_user(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in(request)
        # response object and status code returned
        token = data.get('data')
        if not token:
            return data, status
        return f(*args, **kwargs)
    return decorated


def authenticate_admin(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in(request)
        # response object and status code returned
        token = data.get('data')
        if not token:
            return data, status
        admin = token.get('admin')
        if not admin:
            response = {
                'status': 'failed',
                'message': 'Admin access required'
            }
        return response, 401
    return decorated
