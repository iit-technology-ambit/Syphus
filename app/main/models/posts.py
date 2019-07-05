"""DB Model for the post table
and Junction Tables connecting to User and Post
"""
from . import db
from enums import PostType
from users import User
from errors import LoginError
from imgLinks import imgPostJunction
import datetime

class Post(db.Model):
    """Description of Post model.
    Rows
    -----------
    post_id int [pk]
    authorId varchar [ref: > users.id]
    title varchar
    body text
    post_time timestamp [not null]
    avg_rating float
    num_rating int
    """
    #Columns
    post_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(128), nullable=False)
    body = db.Column(db.Text, nullable=False)
    post_time = db.Column(db.DateTime, default=datetime.datetime.now())
    avg_rating = db.Column(db.Float, default=0.0)
    num_rating = db.Column(db.Integer, default=0)

    #Relationships
    author = db.relationship('User', backref='posts', lazy=False)
    tags = db.relationship('Tag', secondary=postTagJunction, lazy='subquery',
                            backref=db.backref('posts', lazy=True))
    savers = db.relationship('User', secondary=postSaves, lazy=True,
                            backref=db.backref('posts', lazy='subquery'))
    images = db.relationship('ImgLink', secondary=imgPostJunction,
                             lazy='subquery')
    #TODO: Reactions and Ratings

    #Getters and Setters for the fields
    @property
    def author_id(self):
        return self.author

    @author_id.setter
    def author_id(self, authorId):
        try:
            user = User.query.filter(id == authorId).fetchone()
            if user.last_logout != None:
                raise LoginError
        except:
            #Stub to be handled later
            print("Get back to login page")


postTagJunction = db.Table('postTagJunction',
                            db.Column('post_id', db.Integer,
                                      db.ForeignKey('post.post_id'),
                                      primary_key=True),
                            db.Column('tag_id', db.Integer,
                                      db.ForeignKey('tag.id'),
                                      primary_key=True)
)
