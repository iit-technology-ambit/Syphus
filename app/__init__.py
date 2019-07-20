from flask import Blueprint
from flask_restplus import Api

from .main.controller.auth_controller import api as auth_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask-RESTPlus common backend for tech-ambit',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
