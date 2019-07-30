"""DB Model for the post table
and Junction Tables connecting to User and Post
"""
import datetime
from sqlalchemy.ext.hybrid import hybrid_property
from . import *
# from app.main import db
# from app.main.models.enums import PostType
# from app.main.models.users import User
# from app.main.models.errors import LoginError
# from app.main.models.imgLinks import imgPostJunction

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
    _author_id = db.Column(db.String(256), db.ForeignKey(
        'user.username'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.datetime.now())

    avg_rating = db.Column(db.Float, default=0.0)
    num_rating = db.Column(db.Integer, default=0)

    # Relationships
    author = db.relationship('User', backref='posts', lazy=False)
    tags = db.relationship('Tag', secondary=postTagJunction, lazy='subquery',
                           backref=db.backref('posts', lazy=True))
    # savers = db.relationship('User', secondary=postSaves, lazy=True,
    #                          backref=db.backref('posts', lazy='subquery'))
    images = db.relationship('ImgLink', secondary=imgPostJunction,
                             lazy='subquery')

    def __init__(self, author, title, body):
        self.author = author
        self.title = title
        self.body = body

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # Getters and Setters for the fields
    @hybrid_property
    def author_id(self):
        return self.author

    @author_id.setter
    def author_id(self, authorId):
        try:
            user = User.query.filter_by(id=authorId).first()
            if user.last_logout != None:
                raise LoginError
            else:
                self._author_id = authorId

        except:
            # Stub to be handled later
            print("Get back to login page")

    @classmethod
    def getArticlesByTags(cls, tagList, connector='AND'):
        """
        Get all articles that have a tag in tagList.
        If connector is AND intersection of all posts set for each tag will be
        returned. If it is OR, union will be returned
        """
        if connector == 'AND':
            posts = set()
            for tag in tagList:
                if len(posts) == 0:
                    posts = set(cls.query.filter(tag in cls.tags).all())
                else:
                    posts.intersection(
                        set(cls.query.filter(tag in cls.tags).all()))

            return list(posts)
        elif connector == 'OR':
            posts = set()
            for tag in tagList:
                if len(posts) == 0:
                    posts = set(cls.query.filter(tag in cls.tags).all())
                else:
                    posts.union(set(cls.query.filter(tag in cls.tags).all()))

            return list(posts)

    @classmethod
    def getArticles(cls, id):
        return cls.query.filter_by(id=cls.post_id).first()



