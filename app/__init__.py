from flask import Blueprint
from flask_restplus import Api

from app.main.controller.article_controller import api as post_ns
from app.main.controller.auth_controller import api as auth_ns
from app.main.controller.tag_controller import api as tag_ns
from app.main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask-RESTPlus common backend for tech-ambit',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(post_ns, path='/post')
api.add_namespace(tag_ns, path='/tag')
