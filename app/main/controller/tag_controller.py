# endpoint for tag related operations
from flask_restplus import Resource
from flask import request, abort
from app.main import db
from app.main.models.tags import Tag
from app.main.models.users import User

from ..util.tagDto import TagDto


api = TagDto.api
_tag = TagDto.tag


@api.route('/tag/getAll')
class AllTags(Resource):
    @api.doc('list of all tags')
    @api.marshal_list_with(_tag)
    def get(self):
        return Tag.query.all()

@api.route('/tag/remove/<int:id>')
class DeleteTag(Resource):
    def delete(self, id):
        tag = Tag.query.filter_by(id=id).first()
        if tag is not None:
            tag.delete()
            return "Tag deleted", 201
        else:
            abort(404)

@api.route('/tag/add')
class AddTags(Resource):
    @api.doc(params={ 'tags': 'List of tags to be added' })
    def post(self):
        tag_list = request.form['tags']
        for tag in tag_list:
            new_tag = Tag(tag)
        return "tags added", 201

@api.route('/tag/setPriority/<int:id>')
class TagPriority(Resource):
    def post(self, id):
        tagId = request.form['tagId']
        priority = request.form['priorityLevel']
        user = User.query.filter_by(id=id).first()
        user.setTagPriority(tag, priority)
        return "Tag priority set", 201