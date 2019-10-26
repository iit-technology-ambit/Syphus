"""Register all namespaces and import API's from  controllers."""
from flask import Blueprint
from flask_restplus import Api

from app.main.controller.article_controller import api as post_ns
from app.main.controller.auth_controller import api as auth_ns
from app.main.controller.image_controller import api as image_ns
from app.main.controller.issue_controller import api as issue_ns
from app.main.controller.story_controller import api as story_ns
from app.main.controller.tag_controller import api as tag_ns
from app.main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Flask-RESTPlus common backend for Tech-Ambit',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(post_ns, path='/post')
api.add_namespace(tag_ns, path='/tag')
api.add_namespace(issue_ns, path='/issues')
api.add_namespace(image_ns, path='/image')
api.add_namespace(story_ns, path='/stories')
