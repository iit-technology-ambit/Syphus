"""for issue operations"""
from functools import cmp_to_key
from logging import getLogger

from flask import current_app as app

from app.main.models.enums import Month
from app.main.models.newsletters import Newsletter

LOG = getLogger(__name__)

class NewsletterService:

    @staticmethod
    def getLatest():
        try:
            nl = Newsletter.query.order_by(Newsletter.upload_time.desc()).first()
            return nl, 200

        except BaseException:
            LOG.error(
                "Couldn't fetch articles. Please try again later", exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500
        
    @staticmethod
    def add_newsletter(data):
        try:
            nl = Newsletter.query.filter_by(description=data.get('description')).first()
            if nl is not None:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Newsletter already present',
                }
                LOG.info(
                    'Newsletter already present in database. Redirecting to home page')
                return response_object, 300

            nl = Newsletter(data.get('description'), data.get('publish_date'), data.get('newsletter_content'), data.get('cover_image_url'))

            response_object = {
                'status': 'Success',
                'message': 'Issue added Successfully',
            }
            return response_object, 200

        except BaseException:
            LOG.error(
                "Couldn't add new article. Please try again later", exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

