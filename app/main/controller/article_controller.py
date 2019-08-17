from logging import getLogger

from flask import Blueprint, abort, request
from flask_login import current_user, login_required
from flask_restplus import Api, Resource

from app.main.models.errors import LoginError
from app.main.models.imgLinks import ImgLink
from app.main.models.posts import Post
from app.main.models.users import User
from app.main.util.dto import PostDto

LOG = getLogger(__name__)

api = PostDto.api


@api.route("/")
class ArticleFetch(Resource):
    @api.marshal_with(PostDto.article)
    @api.expect(PostDto.articleReq)
    def get(self):
        """
        Fetches the article given by the id.
        """
        post_id = request.args.get('post_id')
        p = Post.getArticles(post_id)
        if p is not None:
            article = {
                "author": p.author.username,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time
            }

            return article
        else:
            abort(404)


@api.route("/create")
class ArticleCreator(Resource):
    # TODO: protect the endpoint from outside access
    @api.expect(PostDto.articleGen, validate=True)
    def post(self):
        user = User.query.filter_by(username=request.json['author']).first()
        p = Post(user, request.json['title'], request.json['body'])
        LOG.info("New Post Created")
        return "Post Created", 201


@api.route("/uploadimg")
class ImageUploader(Resource):
    @api.expect(PostDto.imgGen)
    def post(self):
        img = ImgLink(request.form["image"])
        return f"{ img.link }", 201


@api.route("/save/<int:post_id>")
class ArticleSave(Resource):
    @api.doc()
    @login_required
    def post(self, post_id):
        p = Post.getArticles(post_id)
        current_user.savePost(p)


@api.route("/rate/<int:post_id>")
class ArticleRate(Resource):
    @api.expect(PostDto.rating, validate=True)
    @login_required
    def post(self, post_id):
        p = Post.getArticles(post_id)
        user = User.query.filter_by(username=current_user.username).first()
        user.ratePost(p, int(request.json["score"]))


@api.route("/by_tags")
class ArticleByTag(Resource):
    @api.expect(PostDto.tagList)
    @api.marshal_list_with(PostDto.article)
    def get(self):
        tags = request.args.getlist("tags")
        articles = Post.getArticlesByTags(tags, connector="OR")
        data = list()
        for p in articles:
            article = {
                "author": p.user.first_name + " " + p.user.last_name,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time
            }
            data.append(article)

        return data
