# endpoint for user operations
from flask import request, abort
from flask_login import current_user, login_required
from flask_restplus import Resource

from app.main.util.dto import StoryDto
from app.main.service.story_service import StoryService as Story

api = StoryDto.api
story = StoryDto.story
queryParams = StoryDto.queryParams

@api.route('/addStory')
class AddNewStory(Resource):
    """ Add a new story """
    @api.doc('Endpoint to add a new story')
    @api.expect(story, validate=True)
    def post(self):
        # Adding a new story
        post_data = request.jsosn
        return Story.createStory(data=post_data)

@api.route('/getStories')
class GetStories(Resource):
    """ Get stories using given offset and limit """
    @api.doc('Endpoint to retrieve stories')
    @api.expect(queryParams, validate=True)
    @api.marshal_list_with(story)
    def get(self):
        data = request.json
        resp = Story.retrieveStories(data=data)
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
        if resp[1] !=200:
            return abort(403, resp[0])
        else:
            return resp




