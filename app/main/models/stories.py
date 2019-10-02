"""
DB Model for Users table and
Junction Table relating
Users and Tags
"""
import datetime

from flask_bcrypt import check_password_hash, generate_password_hash
from flask_login import UserMixin
from sqlalchemy.sql import and_, select

from app.main import db, login_manager
from app.main.models.imgLinks import ImgLink, imgStoryJunction


class Story(db.Model, UserMixin):
    """
    Description of Story model.
    Columns
    -----------
    :id: int [pk]
    :title : varchar(255)
    :image : int
    :article_summary : text
    :date : varchar(127)
    :reading_time : int
    """

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    article_summary = db.Column(db.Text)
    date = db.Column(db.String(127))
    reading_time = db.Column(db.Integer) 

    # Relationships
    image = db.relationship('ImgLink', secondary=imgStoryJunction,
                             lazy='subquery')

    # Methods

    def __init__(self, title, article_summary, date, reading_time):
        self.title =  title
        self.article_summary = article_summary
        self.date = date
        self.reading_time = reading_time

        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getStories(offset, limit):
        stories = Story.query.all()
        if stories:
            stories = stories.limit(limit)
            if stories:
                stories = stories.offset(offset)
                return stories
    
    @staticmethod
    def getNumberOfStories():
        stories = Story.query.all()
        return len(stories)