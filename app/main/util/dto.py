# Data Transfer Object- Responsible for carrying data between processes
from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
   	})


class PostDto:
    api = Namespace('article', description='article related operations')

    article = api.model('article', {
        'author': fields.String(required=True,
                                description="Author of the post"),
        'title': fields.String(required=True, description="Title of the post"),
        'body': fields.String(required=True, description="Body of the post"),
        'post_time': fields.DateTime(description="Time Created")
        'imgLinks': fields.List(fields.String, description="ImgLinks")
    })

    articleGen = api.model('articleGen', {
        'author': fields.String(required=True,
                                description="Username author of the post"),
        'title': fields.String(required=True, description="Title of the post"),
        'body': fields.String(required=True, description="Body of the post"),
        'post_time': fields.DateTime(description="Time Created")
    })

    imgGen = api.model('imgGen', {
        'image': fields.Raw(description="Raw Binary Data for images")
    })

    tagList = api.model('tagList', {
        'tags': fields.List(fields.String, description="Tags to searched")
    })
