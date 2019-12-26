'''
All Endpoints required for newsletter
operations such as getting latest newsletter and
adding new newsletter.
'''

from flask import request
from flask_restplus import Resource

from app.main.controller.auth_controller import Authentication
from app.main.service.newsletter_service import NewsletterService
from app.main.util.dto import NewsletterDto

api = NewsletterDto.api
newsletter = NewsletterDto.newsletter


@api.route('/getLatest')
class getLatestNL(Resource):
    """ Endpoint to fetch the latest newsletter"""
    @api.doc("getting latest newletter")
    @api.marshal_with(newsletter, envelope='resource')
    def get(self):
        return NewsletterService.getLatest()


@api.route('/add')
class addNL(Resource):
    """ Endpoint to add an newsletter """
    @api.doc("Adding a new newsletter")
    @api.expect(newsletter, validate=True)
    @Authentication.isSuperUser
    def post(self):
        post_data = request.json
        return NewsletterService.add_newsletter(post_data)
