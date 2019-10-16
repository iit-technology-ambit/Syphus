# endpoint for user operations
from flask import abort, request
from flask_login import current_user, login_required
from flask_restplus import Resource

from app.main.service.auth_service import Authentication
from app.main.service.story_service import StoryService as Story
from app.main.util.dto import StoryDto

api = StoryDto.api
story = StoryDto.story

@api.route('/addStory')
class AddNewStory(Resource):
    """ Add a new story """
    @api.doc('Endpoint to add a new story')
    @api.expect(story, validate=True)
    @Authentication.isSuperUser
    def post(self):
        # Adding a new story
        post_data = request.json
        return Story.createStory(data=post_data)


@api.route('/getStories')
class GetStories(Resource):
    """ Get stories using given offset and limit """
    @api.doc('Endpoint to retrieve stories')
    @api.marshal_list_with(story)
    def get(self):
        if request.args.get('offset', False):
            offset = request.args['offset']
        else:
            offset = 0

        if request.args.get('limit', False):
            limit = request.args['limit']
        else:
            limit = None

        resp = Story.retrieveStories(offset=offset, limit=limit)
        if resp[1] != 200:
            return abort(403, resp[0])
        else:
            return resp


@api.route('/numberOfStories')
class NumberOfStories(Resource):
    """ Get total number of stories """
    @api.doc('Endpoint to get total number of stories in DB')
    def get(self):
        resp = Story.getTotalNumber()
        if resp[1] != 200:
            return abort(403, resp[0])
        else:
            return resp
