"""DB Model for the post table
and Junction Tables connecting to User and Post
"""
import datetime
from random import sample

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import and_, join, or_, select

# from . import *
from app.main import db
from app.main.models.enums import PostType
# from app.main.models.users import User
from app.main.models.errors import LoginError
from app.main.models.imgLinks import ImgLink, imgPostJunction
from app.main.models.tags import Tag

postTagJunction = db.Table('postTagJunction',
                           db.Column('post_id', db.Integer,
                                     db.ForeignKey('post.post_id'),
                                     primary_key=True),
                           db.Column('tag_id', db.Integer,
                                     db.ForeignKey('tag.id'),
                                     primary_key=True)
                           )


class Post(db.Model):
    """
    Description of Post model.
    Rows
    -----------
    :post_id: int [pk]
    :authorId: varchar [ref: > users.id]
    :title: varchar
    :body: text
    :post_time: timestamp [not null]
    :avg_rating: float
    :num_rating: int
    """
    # Columns
    post_id = db.Column(db.Integer, primary_key=True)
    # _author_id = db.Column(db.String(256), db.ForeignKey(
    #     'user.username'), nullable=False)
    author_name = db.Column(db.String(256), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.datetime.now())

    avg_rating = db.Column(db.Float, default=0.0)
    num_rating = db.Column(db.Integer, default=0)

    # Relationships
    # author = db.relationship('User', backref='posts', lazy=False)
    tags = db.relationship('Tag', secondary=postTagJunction, lazy='subquery',
                           backref=db.backref('posts', lazy=True))
    images = db.relationship('ImgLink', secondary=imgPostJunction,
                             lazy='subquery')

    def __init__(self, author, title, body):
        self.author_name = author
        self.title = title
        self.body = body

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getArticlesByTags(tagList, connector='OR'):
        """
        Get all articles that have a tag in tagList.
        If connector is AND intersection of all posts set for each tag will be
        returned. If it is OR, union will be returned
        """
        stmt = select([Post,
                       postTagJunction.c.post_id.label("pid"),
                       postTagJunction.c.tag_id]).distinct().where(and_(postTagJunction.c.post_id == Post.post_id,
                                                                        postTagJunction.c.tag_id.in_(tagList)))
        result = db.session.execute(stmt)
        results = result.fetchall()
        # return results
        # taking only unique values
        unique_results = dict()
        # print(results.c)
        for result in results:
            # print(dict(result))
            if unique_results.get(result.post_id, 0) == 0:
                unique_results[result.post_id] = result
        # print(unique_results[1].post_id)
        return unique_results.values()

    @staticmethod
    def getArticles(post_id):
        return Post.query.filter_by(post_id=post_id).first()

    @staticmethod
    def getRandomizedArticles(size):
        return sample(Post.query.all(), size)

    def addTags(self, list_of_tags):
        self.tags.extend(list_of_tags)
        db.session.commit()

    def associateImage(self, imgId):
        img = ImgLink.query.filter_by(id=imgId).first()
        self.images.append(img)
        db.session.commit()

    def tagDump(self):
        dump = []
        for tag in self.tags:
            dump.append(tag.name)
        return dump

    def linkDump(self):
        dump = []
        for img in self.images:
            dump.append(img.link)

        return dump
