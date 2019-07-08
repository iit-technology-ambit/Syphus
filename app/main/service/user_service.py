# for user related operations

import uuid
import datetime

from app.main import db
from app.main.models.user import User

def save_new_user(data):
    """Creates a new user"""
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            # generates a random id
            public_id=str(uuid.uuid4())
            email=data['email'],
            username=data['username']
            password=data['password']
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response = {
            'status': 'success',
            'message': 'User successfully created'
        }
        return response_object, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists'
        }
        return response, 409

def get_all_users():
    return User.query.all()

def get_user(id):
    return User.query.filter_by(public_id=id)
