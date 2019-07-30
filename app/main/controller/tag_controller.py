# endpoint for tag related operations
from flask_restplus import Resource
from flask import request, abort
from flask_login import current_user, login_required
from app.main import db
from app.main.models.tags import Tag
from app.main.models.users import User

from app.main.util.dto import TagDto


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
	@api.doc(params={ 'tags': 'List of tags to be added' })
	@api.marshal_list_with(tag)
	def post(self):
		tag_list = request.json
		for tag in tag_list:
			new_tag = Tag(tag)
		return "tags added", 201

@api.route('/setPriority/<id>')
class TagPriority(Resource):
	@login_required
	def post(self, id):
		tag = Tag.query.filter_by(id=id).first()
		priority = request.headers['priorityLevel']
		current_user.setTagPriority(tag, priority)
		return "Tag priority set", 201