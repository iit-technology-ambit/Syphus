from flask_restplus import Namespace, fields

class TagDto:
    api = Namespace('tag', description='for tag related operations')
    tag = api.model('tag', {
        'id': fields.Integer(required=True, description='tag id'),
        'name': fields.String(required=True, description='tag name')
    })