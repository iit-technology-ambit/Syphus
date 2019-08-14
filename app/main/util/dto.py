# Data Transfer Object- Responsible for carrying data between processes
from flask_restplus import Namespace, fields


class AuthDto:
	api = Namespace('auth', description='Authentication Related operations')
	user_auth = api.model('auth_details', {
		'email': fields.String(required=True, description='Login Email'),
		'password': fields.String(required=True, description='Login Password'),
		'remember': fields.String(description='Stay Logged In'),
	})
	
	reset_email = api.model('email_details', {
		'email': fields.String(required=True, description='Login Email')
	})
 

class UserDto:
	api = Namespace('user', description='user related operations')
	user = api.model('user', {
		'username': fields.String(required=True, description='user username'),
		'password': fields.String(required=True, description='user password'),
		'email': fields.String(required=True, description='user email address'),
	})
 
	userInfo = api.model('userInfo', {
		'username': fields.String(required=True, description='user username'),
		'first_name': fields.String(description='first name', default=""),
		'last_name': fields.String(description="last name", default=""),
		'dob': fields.DateTime(dt_format='rfc822', description="date of birth"),
		'email': fields.String(required=True, description='user email address'),
		'fb_handle': fields.String(description="facebook handle"),
		'g_handle': fields.String(description="github handle"),
		'medium_handle': fields.String(description="medium handle"),
		'twitter_handle': fields.String(description="twitter handle"),
		'linkedin_handle': fields.String(description="linkedin handle"),
		'bio': fields.String(description="biography"),
		'occupation': fields.String(description="occupation"),
		'last_login': fields.DateTime(dt_format='rfc822', description="last login time")
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

	rating = api.model('rating',  {
		'score': fields.Integer(required=True, description="Rating of the post")
	})

class TagDto:
	api = Namespace('tag', description='for tag related operations')
	tag = api.model('tag', {
		'name': fields.String(required=True, description='tag name'),
	})
	priority = api.model('priority', {
		'tag_id': fields.Integer(required=True, description="id of the concerned tag"),	
		'value': fields.Integer(required=True, description="priority level of the tag")
	})

class IssueDto:
	api = Namespace('issue', description="for issue related operations")
	issue = api.model('tag', {
		'id' : fields.Integer(required=True, description="ID of the concerned tag"),
		'cover' : fields.Integer(required=True, description="Cover image of the concerned issue"),
		'month' : fields.String(required=True, description="Month of the concerned issue"),
		'year' : fields.String(required=True, description="Year of the concerned issue"),
		'issue_tag' : fields.String(required=True, description="Tag associated with the concerned issue"),
		'link' : fields.String(required=True, description="Link of the concerned issue")
	})