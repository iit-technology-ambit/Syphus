"""for issue operations"""

from logging import getLogger

from flask import current_app as app

from app.main.models.issues import Issue

LOG = getLogger(__name__)


class IssueService:

    @staticmethod
    def getAll():
        try:
            issues = Issue.query.all()
            return issues, 200

        except BaseException:
            LOG.error(
                "Couldn't fetch articles. Please try again later", exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def addIssue(data):
        try:
            issue = Issue.query.filter_by(link=data.get('link')).first()
            if issue is not None:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Issue already present',
                }
                LOG.info(
                    'Issue already present in database. Redirecting to home page')
                return response_object, 300

            issue = Issue(data.get('coverId'), data.get('month'),
                          data.get('year'), data.get('link'))
            if data.get('description') is not None:
                issue.setDescription(data.get('description'))

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
