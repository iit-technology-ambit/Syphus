from flask_restplus import Api, Resource
from flask_login import current_user, login_required
from flask import Blueprint, request, abort
from app.main.util.dto import PostDto
from app.main.models.posts import Post
from app.main.models.users import User
from app.main.models.imgLinks import ImgLink
from app.main.models.errors import LoginError
from logging import getLogger

LOG = getLogger(__name__)

api = PostDto.api


@api.route("/<int:post_id>")
class ArticleFetch(Resource):
    @api.marshal_with(PostDto.article)
    @api.doc(params={'post_id': 'Post Id'})
    def get(self, post_id):
        """
        Fetches the article given by the id.
        """
        p = Post.getArticles(id)
        if p is not None:
            article = {
                "author": p.user.first_name + " " + p.user.last_name,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time
            }

            return article
        else:
            abort(404)


@api.route("/create")
class ArticleCreator(Resource):
    @api.expect(PostDto.articleGen)
    def post(self):
        user = User.query.filter_by(username=request.form['author'])
        p = Post(user, request.form['title'], request.form['body'])

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
    @api.doc(params={"rating": "Rating Value"})
    @login_required
    def post(self, post_id):
        p = Post.getArticles(post_id)
        current_user.ratePost(p, int(request.form["rating"]))


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
