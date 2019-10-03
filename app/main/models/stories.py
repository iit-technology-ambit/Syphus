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


class Story(db.Model, UserMixin):
    """
    Description of Story model.
    Columns
    -----------
    :id: int [pk]
    :title : varchar(255)
    :image_link : varchar(255)
    :article_summary : text
    :date : varchar(255)
    :reading_time : int
    """

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    article_summary = db.Column(db.Text)
    image_link = db.Column(db.String(255))
    date = db.Column(db.String(255))
    reading_time = db.Column(db.Integer)

    # Methods

    def __init__(self, title, article_summary, image_link, date, reading_time):
        self.title = title
        self.article_summary = article_summary
        self.image_link = image_link
        self.date = date
        self.reading_time = reading_time

        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getStories(offset, limit):
        if limit is not None:
            stories = Story.query.order_by(Story.date.desc()).limit(limit).offset(offset).all()
            return stories
        return Story.query.order_by(Story.date.desc()).offset().all()
    @staticmethod
    def getNumberOfStories():
        stories = Story.query.all()
        return len(stories)
