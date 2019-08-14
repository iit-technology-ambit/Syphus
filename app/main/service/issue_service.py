# for issue operations
import traceback
from logging import getLogger

from flask import current_app as app
from app.main.models.issues import Issue

LOG = getLogger(__name__)

class IssueService:
    
    @staticmethod
    def getAll():
        try:
            issues = Issue.query.all()
            return issues,200

        except:
            LOG.error("Couldn't fetch articles. Please try again later")
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def addIssue(data):
        try:
            issue = Issue.query.filter_by(id=data.get['id']).first()
            if issue is not None:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Issue already present',
                }
                LOG.info('Issue already present in databse. Redirecting to home page')
                return response_object, 300
            
            issue = Issue(data.get('cover'), data.get('month'), data.get('year'), data.get('link'))
            response_object = {
                'status': 'Success',
                'message': 'Issue added Successfully',
            }
            return response_object, 200

        except:
            LOG.error("Couldn't add new article. Please try again later")
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500



