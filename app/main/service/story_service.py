from logging import getLogger

from flask import abort
from flask import current_app as app

from app.main.models.stories import Story

LOG = getLogger(__name__)


class StoryService:

    @staticmethod
    def createStory(data):
        try:
            storyCard = Story.query.filter_by(title=data.get('title')).first()
            if storyCard is not None:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Story Already Present',
                }
                LOG.info(
                    'Story already present. Redirecting to home page')
                return response_object, 300

            storyCard = Story(data.get('title'), data.get('article_summary'), data.get('image_link'),
                              data.get('date'), data.get('reading_time'))

            response_object = {
                'status': 'Success',
                'message': 'Story Added Successfully'
            }
            return response_object, 201

        except BaseException:
            LOG.error(
                'Story couldn\'t be added. Please try again later', exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def retrieveStories(data):
        try:
            offset = data.get('offset')
            limit = data.get('limit')
            stories = Story.getStories(offset=offset, limit=limit)
            if stories is not None:
                return stories, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Empty Respone'
                }
                return response_object, 400

        except BaseException:
            LOG.error(
                'Stories couldn\'t be retrieved. Please try again later', exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def getTotalNumber():
        try:
            number = Story.getNumberOfStories()
            if number > 0:
                return number, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'No stories in DB'
                }
                return response_object, 400

        except BaseException:
            LOG.error(
                'Stories couldn\'t be retrieved. Please try again later', exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500
