from flask_restplus import Api, Resource
from flask import Blueprint, request, abort
from app.main.util.dto import PostDto
from app.main.models.posts import Post
from app.main.models.users import User
from app.main.models.imgLinks import ImgLink
from app.main.models.errors import LoginError
from logging import getLogger

LOG = getLogger(__name__)

bp = Blueprint("article", __name__, url_prefix='/article')
api = Api(bp)
api.add_namespace(PostDto.api)

@api.route("/<int:post_id>")
class ArticleFetch(Resource):
    @api.marshal_with(PostDto.article)
    @api.doc(params={'post_id': 'Post Id'})
    def get(self, post_id):
        """
        Fetches the article given by the id.
        """
        post = Post.getArticles(id)
        article = {
            "author" : post.user.first_name + " " + post.user.last_name,
            "title": post.title,
            "body": post.body,
            "post_time": post.post_time
        }

        if article is not None:
            return article
        else:
            abort(404)

@api.route("/create")
class ArticleCreator(Resource):
    @api.expect(PostDto.articleGen)
    def post(self):
        user = User.query.filter_by(username=request.form['author'])
        post = Post(user, request.form['title'], request.form['body'])

        if "images" in request.form:
            for image in request.form.images:
                post.images.append(ImgLink(image))

        LOG.info("New Post Created")
        return "Post Created", 201

@api.route("/save/<int:post_id>")
class ArticleSave(Resource):
    @api.doc(params={"id": "post_id"})
    def post(self, post_id):
        post = Post.getArticles(id)
        #First define what data is to be sent for user validation
        raise LoginError

@api.route("/rate/<int:post_id>")
class ArticleRate(Resource):
    @api.doc(params={"id": "post_id"})
    def post(self, post_id):
        raise LoginError

@api.route("/by_tags")
class ArticleByTag(Resource):
    @api.doc(






