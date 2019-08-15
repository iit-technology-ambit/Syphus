'''
All Endpoints required for issue
operations such as getting all issues and
adding new issues.
'''

from flask import request
from flask_restplus import Resource

from app.main.service.issue_service import IssueService
from app.main.util.dto import IssueDto

api = IssueDto.api
issue = IssueDto.issue


@api.route('/getAll')
class getAllIssues(Resource):
    """ Endpoint to get all issues """
    @api.doc("Getting all issues")
    @api.marshal_with(issue, envelope='resource')
    def get(self):
        return IssueService.getAll()


@api.route('/add')
class addIssue(Resource):
    """ Endpoint to add an issue """
    @api.doc("Adding a new issue")
    @api.expect(issue, validate=True)
    def post(self):
        post_data = request.json
        return IssueService.addIssue(data=post_data)
