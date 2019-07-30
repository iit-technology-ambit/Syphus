# Data Transfer Object- Responsible for carrying data between processes
from flask_restplus import Namespace, fields


class AuthDto:
	api = Namespace('auth', description='Authentication Related operations')
	user_auth = api.model('auth_details', {
		'email': fields.String(required=True, description='Login Email'),
		'password': fields.String(required=True, description='Login Password'),
		'remember': fields.String(description='Stay Logged In'),
	})



class UserDto:
	api = Namespace('user', description='user related operations')
	user = api.model('user', {
		'id': fields.String(description='user Identifier'),
		'username': fields.String(required=True, description='user username'),
		'password': fields.String(required=True, description='user password'),
		'email': fields.String(required=True, description='user email address'),
	})
	
	payment = api.model('payment', {
		'username': fields.String(required=True,
								  description='username of the payee'),
		'amount': fields.Float(required=True, descripton="Amount paid"),
		'api_response': fields.String(required=True,
									  description="Response returned by vendor")
	})

class PostDto:
	api = Namespace('article', description='article related operations')
	article = api.model('article', {
		'author': fields.String(required=True,
								description="Author of the post"),
		'title': fields.String(required=True, description="Title of the post"),
		'body': fields.String(required=True, description="Body of the post"),
		'post_time': fields.DateTime(description="Time Created"),
		'imgLinks': fields.List(fields.String, description="ImgLinks"),
	})

	articleGen = api.model('articleGen', {
		'author': fields.String(required=True,
								description="Username author of the post"),
		'title': fields.String(required=True, description="Title of the post"),
		'body': fields.String(required=True, description="Body of the post"),
		'post_time': fields.DateTime(description="Time Created"),
	})

	imgGen = api.model('imgGen', {
		'image': fields.Raw(description="Raw Binary Data for images"),
	})

	tagList = api.model('tagList', {
		'tags': fields.List(fields.String, description="Tags to searched"),
	})

class TagDto:
	api = Namespace('tag', description='for tag related operations')
	tag = api.model('tag', {
		'id': fields.Integer(required=True, description='tag id'),
		'name': fields.List(fields.String(required=True, description='tag name')),
	})
	tag_list = api.model('TagList', {
	'tags': fields.List(fields.Nested(tag)),
	})