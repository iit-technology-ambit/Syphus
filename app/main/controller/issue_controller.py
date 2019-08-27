'''
All Endpoints required for issue
operations such as getting all issues and
adding new issues.
'''

from flask import request
from flask_restplus import Resource

from app.main.models.imgLinks import ImgLink
from app.main.service.auth_service import Authentication
from app.main.service.issue_service import IssueService
from app.main.util.dto import IssueDto

api = IssueDto.api
issue = IssueDto.issue
issue_new = IssueDto.issue_new


@api.route('/getAll')
class getAllIssues(Resource):
    """ Endpoint to get all issues """
    @api.doc("Getting all issues")
    @api.marshal_list_with(issue, envelope='resource')
    def get(self):
        all_issues = IssueService.getAll()[0]
       
        for ind in range(len(all_issues)):
            all_issues[ind].cover_link = ImgLink.query.filter_by(
                id=all_issues[ind].cover).first().link

        return all_issues


@api.route('/add')
class addIssue(Resource):
    """ Endpoint to add an issue """
    @api.doc("Adding a new issue")
    @api.expect(issue_new, validate=True)
    @Authentication.isSuperUser
    def post(self):
        post_data = request.json
        return IssueService.addIssue(data=post_data)
