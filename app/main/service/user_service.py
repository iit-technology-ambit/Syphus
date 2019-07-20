# for user related operations

import datetime

from app.main import db
from app.main.models.user import User

def save_new_user(data):
    """Creates a new user"""
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response = {
            'status': 'success',
            'message': 'User successfully created'
        }
        return response, 201
    else:
        response = {
            'status': 'fail',
            'message': 'User already exists'
        }
        return response, 409

def get_all_users():
    """Gets all users"""
    return User.query.all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
