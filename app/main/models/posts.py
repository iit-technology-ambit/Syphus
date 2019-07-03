"""DB Model for the post table"""
from . import db
from enums import PostType
from tags import tagPostJunction
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
    tags = db.relationship('Tag', secondary=tagPostJunction, lazy='subquery',
                            backref=db.backref('posts', lazy=True))
    #TODO: user<->post relation
