# endpoint for tag related operations
from app.main import db
from app.main.models.tags import Tag
from app.main.models.users import User
from app.main.util.dto import TagDto
from flask import abort, request
from flask_login import current_user, login_required
from flask_restplus import Resource

api = TagDto.api
tag = TagDto.tag


@api.route('/getAll')
class AllTags(Resource):
	@api.doc('list of all tags')
	@api.marshal_list_with(tag)
	def get(self):
		return list(Tag.query.all())

@api.route('/remove/<int:id>')
class DeleteTag(Resource):
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
	def post(self):
		tag = request.json['name']
		new_tag = Tag(tag)
		response_object = {
			'status' : 'Success',
			'message' : 'Tag added successfully',
		}
		return response_object,200
		
@api.route('/setPriority/<id>')
class TagPriority(Resource):
	@login_required
	def post(self, id):
		tag = Tag.query.filter_by(id=id).first()
		priority = request.headers['priorityLevel']
		current_user.setTagPriority(tag, priority)
		return "Tag priority set", 201
