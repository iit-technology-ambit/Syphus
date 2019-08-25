from logging import getLogger

from flask import Blueprint, abort, request, current_app
from flask_login import current_user, login_required
from flask_restplus import Api, Resource
from sqlalchemy import desc
from werkzeug.datastructures import FileStorage

from app.main.models.errors import LoginError
from app.main.models.imgLinks import ImgLink
from app.main.models.posts import Post
from app.main.models.users import User
from app.main.models.tags import Tag
from app.main.util.dto import PostDto

LOG = getLogger(__name__)

api = PostDto.api

@api.route("/")
class ArticleFetch(Resource):
    @api.marshal_with(PostDto.article)
    @api.doc(params={'post_id': 'Id of the requested post'})
    def get(self):
        """
        Fetches the article given by the id.
        """
        post_id = request.args.get('post_id')
        p = Post.getArticles(int(post_id))
        if p is not None:
            article = {
                "post_id": p.post_id,
                "author_id": p.author.id,
                "author": p.author.username,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time,
                "imgLinks": p.linkDump(),
                "tags": p.tagDump(),
                "isSaved": p in current_user.saves if "saves" in current_user.__dict__ else False 
            }

            return article
        else:
            abort(404)

@api.route("/getAll")
class ArticleFetchAll(Resource):
    @api.marshal_list_with(PostDto.article)
    @api.doc(params={'num': 'Number of articles to fetch'})
    def get(self):
        if request.args.get('num') is None or int(request.args.get('num')) <= 0:
            posts = Post.query.order_by(desc(Post.avg_rating)).all()
        else:
            posts = Post.query.order_by(desc(Post.avg_rating)).\
                    limit(int(request.args.get('num'))).all()

        articles = []
        for p in posts:
            article = {
                "post_id": p.post_id,
                "author_id": p.author.id,
                "author": p.author.username,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time,
                "imgLinks": p.linkDump(),
                "tags": p.tagDump(),
                "isSaved": p in current_user.saves if "saves" in current_user.__dict__ else False
            }
            articles.append(article)
        
        return articles

@api.route("/create")
class ArticleCreator(Resource):
    # TODO: protect the endpoint from outside access
    @api.expect(PostDto.articleGen, validate=True)
    def post(self):
        user = User.query.filter_by(username=request.json['author']).first()
        if user is None:
            return {'message': 'Author not found!'}, 404
        p = Post(user, request.json['title'], request.json['body'])
        LOG.info("New Post Created")
        return "Post Created", 201


@api.route("/associateImg")
class ImgAssociator(Resource):
    """DISABLE CORS FOR THIS."""
    @api.expect(PostDto.imgAs)
    def post(self):
        p = Post.query.filter_by(post_id=request.json['post_id']).first()
        p.associateImage(request.json['img_id'])
        return "Image Associated", 201


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
    def post(self):

        tags = request.json["tags"]
        tagList = []
        for tag in tags:
            try:
                tagList.append(Tag.query.filter_by(name=tag).first().id)
            except:
                pass

        articles = Post.getArticlesByTags(tagList, connector="OR")
        data = list()
        for p in articles:
            # print(p.post_id)
            aid = User.query.filter_by(username=p._author_id).first().id
            article = {
                "post_id": p.post_id,
                "author": p._author_id,
                "author_id": aid,
                "title": p.title,
                "body": p.body,
                "post_time": p.post_time
            }
            data.append(article)

        return data


@api.route("/add_tag")
class ArticleAddTag(Resource):
    @api.expect(PostDto.addtaglist)
    def put(self):
        p = Post.getArticles(request.json['post_id'])
        t = []
        for tag in request.json['tags']:
            t.append(Tag.query.filter_by(name=tag).first())

        p.addTags(t)
        return "Tags added sucessfully", 201
