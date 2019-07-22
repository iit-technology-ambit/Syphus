# endpoint for tag related operations
from flask_restplus import Resource
from app.main import db
from app.main.models.tags import Tag

from ..util.tagDto import TagDto


api = TagDto.api
_tag = TagDto.tag

# Routes

@api.route('/tag/getAll')
class AllTags(Resource):
    @api.doc('list of all tags')
    @api.marshal_list_with(_tag)
    def get(self):
        """Gets all tags"""
        # Make db call
        return Tag.query.all()