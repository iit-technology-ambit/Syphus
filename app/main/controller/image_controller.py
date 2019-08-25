from logging import getLogger

from flask import Blueprint, abort, request, current_app
from flask_login import current_user, login_required
from flask_restplus import Api, Resource
from sqlalchemy import desc
from werkzeug.datastructures import FileStorage

from app.main.models.errors import LoginError
from app.main.models.imgLinks import ImgLink
from app.main.util.dto import ImageDto

LOG = getLogger(__name__)
api = ImageDto.api
fileParser = ImageDto.getFileParser()

@api.route("/uploadImg")
class ImageUploader(Resource):
    """DISABLE CORS FOR THIS."""
    @api.expect(fileParser)
    def post(self):
        f = request.files['file']
        img = ImgLink(f)
        return f"{ img.link }", 201


@api.route("/addLink")
class AddImageLink(Resource):
    """DISABLE CORS FOR THIS."""
    @api.expect(ImageDto.linkOfImage)
    def post(self):
        img = ImgLink(link=request.json['link'])
        LOG.info("New link added without verification")
        return f"{ img.id }", 201
