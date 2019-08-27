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
from app.main.models.enums import PriorityType
from app.main.models.payments import Payment
from app.main.models.posts import Post
from app.main.models.tags import Tag

userTagJunction = db.Table('userTagJunction',
                           db.Column('user_id', db.Integer,
                                     db.ForeignKey('user.id'), primary_key=True),
                           db.Column('keyword_id', db.Integer, db.ForeignKey('tag.id'),
                                     primary_key=True),
                           db.Column('priority', db.Enum(PriorityType),
                                     default=PriorityType.follow)
                           )

userPostInteraction = db.Table('userPostInteraction',
                               db.Column('user_id', db.Integer,
                                         db.ForeignKey('user.id'), primary_key=True),
                               db.Column('post_id', db.Integer,
                                         db.ForeignKey('post.post_id'), primary_key=True),
                               db.Column('rating', db.Integer, default=0),
                               db.Column('save', db.Boolean, default=True)
                               )


class User(db.Model, UserMixin):
    """
    Description of User model.
    Columns
    -----------
    :id: int [pk]
    :username: varchar(128) [not NULL]
    :password: varchar(128) [not NULL]
    :first_name: varchar(255) [not NULL]
    :last_name: varchar(255)
    :dob: date
    :email: varchar(255) [not NULL]
    :fb_handle: varchar(255)
    :g_handle: varchar(255)
    :medium_handle: varchar(255)
    :twitter_handle: varchar(255)
    :linkedin_handle: varchar(255)
    :bio: text
    :occupation: varchar(255)
    :profile_picture: int
    :last_login: timestamp
    :creation_time: timestamp
    :is_verified: boolean
    """

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(255), default="")
    last_name = db.Column(db.String(255), default="")
    dob = db.Column(db.DateTime)
    email = db.Column(db.String(255), nullable=False)
    fb_handle = db.Column(db.String(255))
    g_handle = db.Column(db.String(255))
    medium_handle = db.Column(db.String(255))
    twitter_handle = db.Column(db.String(255))
    linkedin_handle = db.Column(db.String(255))
    profile_picture = db.Column(db.Integer)
    bio = db.Column(db.Text)
    occupation = db.Column(db.String(255))
    last_login = db.Column(db.DateTime)
    creation_time = db.Column(db.DateTime)
    is_verified = db.Column(db.Boolean, default=False)

    # Relationships
    tags = db.relationship('Tag', secondary=userTagJunction, lazy='subquery',
                           backref=db.backref("users", lazy=True))

    saves = db.relationship('Post', secondary=userPostInteraction, lazy=True,
                            backref=db.backref("savers", lazy=True))

    payments = db.relationship('Payment', backref='user', lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.is_verified = False
        self.profile_picture = 1

        db.session.add(self)
        db.session.commit()

    @staticmethod
    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(id=id).first()

    def update_col(self, key, value):
        self.__dict__[key] = value
        db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def resetPassword(self, newPassword):
        # Pass in a hashed password
        self.password = generate_password_hash(newPassword)
        db.session.commit()

    def addPayment(self, data):
        pay = Payment(self, data.get("amount"), data.get("api_response"))
        self.payments.append(pay)
        db.session.commit()

    def get_id(self):
        return self.id

    # We do not need to implement update metadata.
    # Actually, it can be updated ad hoc by assignment without calling commit.
    def isVerified(self):
        return self.is_verified

    def setVerified(self):
        self.is_verified = True
        db.session.commit()

    def setNewTag(self, tag):
        self.tags.append(tag)
        db.session.commit()

    def setTagPriority(self, tag, priority):
        result = self.getTagPriority(tag)

        if result is None:
            self.setNewTag(tag)

        s = userTagJunction.update().\
            values(priority=PriorityType(priority)).\
            where(and_(
                userTagJunction.c.user_id == self.id,
                userTagJunction.c.keyword_id == tag.id))

        db.session.execute(s)
        db.session.commit()

    def getTagPriority(self, tag):
        s = select([userTagJunction]).where(and_(
            userTagJunction.c.user_id == self.id,
            userTagJunction.c.keyword_id == tag.id))
        result = list(db.session.execute(s))
        try:
            return result[0]["priority"]
        except IndexError:
            return None

    def savePost(self, post):
        if post not in self.saves:
            self.saves.append(post)
        else:
            self.saves.remove(post)
        db.session.commit()

    def ratePost(self, post, rating):
        try:
            s = userPostInteraction.update().\
                where(user_id=self.id, post_id=post.post_id).\
                values(rating=rating)
            db.session.execute(s)
        except BaseException:
            # User has not yet saved the post so there is no entry here
            s = userPostInteraction.insert().\
                values(save=False, rating=rating,
                       user_id=self.id, post_id=post.post_id)
            db.session.execute(s)
        finally:
            db.session.commit()
