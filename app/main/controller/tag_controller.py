# endpoint for tag related operations
from app.main import db
from app.main.models.tags import Tag
from app.main.models.users import User
from app.main.models.enums import PriorityType
from app.main.util.dto import TagDto
from flask import abort, request
from flask_login import current_user, login_required
from flask_restplus import Resource
from logging import getLogger

LOG = getLogger(__name__)

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
		
@api.route("/usertagops/<tag_id>")
class UserTagActions(Resource):
	@login_required
	@api.doc(params={'id': 'id of the tag to be added'})
	def post(self, tag_id):
		try:
			tag = Tag.query.filter_by(id=tag_id).first()
			current_user.setNewTag(tag)
			return "Success", 201
		except:
			LOG.warning("Illegal tag id was requested")
			return "Invalid", 403
	
	@login_required
	@api.doc(params={'id': 'id of the tag whose priority is to be modified'})
	@api.expect(TagDto.priority)
	def put(self, tag_id):
		try:
			tag = Tag.query.filter_by(id=tag_id).first()
			pr = PriorityType.follow
			if request.form["priority"] < 0:
				pr = PriorityType.less_of_these
			elif request.form["priority"] > 0:
				pr = PriorityType.more_of_these

			current_user.setTagPriority(tag, pr)
			return "Success", 201
		except:
			LOG.warning("Illegal tag id was requested")
			return "Invalid", 403


