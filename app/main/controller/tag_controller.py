# endpoint for tag related operations
from flask import abort, request
from flask_login import current_user, login_required
from flask_restplus import Resource

from app.main import db
from app.main.models.enums import PriorityType
from app.main.models.tags import Tag
from app.main.models.users import User
from app.main.service.auth_service import Authentication
from app.main.util.dto import TagDto

api = TagDto.api
tag = TagDto.tag
priorityLevel = TagDto.priority


@api.route('/getAll')
class AllTags(Resource):
    @api.doc('list of all tags')
    @api.marshal_list_with(tag)
    def get(self):
        return list(Tag.query.all())


@api.route('/remove/<int:id>')
class DeleteTag(Resource):
    @Authentication.isSuperUser
    def delete(self, id):
        tag = Tag.query.filter_by(id=id).first()
        if tag is not None:
            tag.delete()
            return "Tag deleted", 201
        else:
            abort(404)


@api.route('/add', methods=['POST'])
class AddTags(Resource):
    @api.doc('Endpoint to add a particular tag')
    @api.expect(tag, validate=True)
    @Authentication.isSuperUser
    def post(self):
        tag = request.json['name']
        new_tag = Tag(tag)
        response_object = {
            'status': 'Success',
            'message': 'Tag added successfully',
        }
        return response_object, 200


@api.route('/setPriority')
class TagPriority(Resource):
    @login_required
    @api.doc('Set status of the tag for the logged in user.')
    @api.expect(priorityLevel, validate=True)
    def post(self):
        tag_id = request.json['tag_id']
        priority = request.json['value']
        if priority not in [-1, 0, 1]:
            return "Invalid tag priority value", 400

        tag = Tag.query.filter_by(id=tag_id).first()
        if tag is None:
            return "Tag id not found", 404
        current_user.setTagPriority(tag, priority)
        return "Tag priority set", 201
