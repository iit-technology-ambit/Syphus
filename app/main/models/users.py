"""
DB Model for Users table and
Junction Table relating
Users and Tags
"""
from . import db
from enums import PriorityType
from posts import Post
from tags import Tag
from sqlalchemy.sql import select
import datetime

class User(db.Model):
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
	"""

	#Columns
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), nullable=False)
	password = db.Column(db.String(128), nullable=False)
	first_name = db.Column(db.String(255), nullable=False)
	last_name = db.Column(db.String(255), nullable=False)
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

	#Relationships
	tags = db.relationship('Tag', secondary=userTagJunction, lazy='subquery',
							backref=db.backref("users", lazy=True))

	saves = db.relationship('Post', secondary=userPostInteraction, lazy=True,
							backref=db.backref("savers", lazy=True))

	#To get all payments done by user, call User.payments
	#This is defined in payments.py as db.relationship

	def __init__(self, username, password, email):
		self.username = username
		self.password = password
		self.email = email

		db.session.add(self)
		db.session.commit()

	def resetPassword(self, newPassword):
		#Pass in a hashed password
		self.password = newPassword
		db.session.commit()

	def updateMetaData(self, **kwargs):
		# TODO
		pass
	def getMetaData(self):
		# TODO
		pass

	# TODO: Do something about isVerifiedEmail 

	def setNewTag(self, tag):
		self.tags.append(tag)
		db.session.commit()
	def setTagPriority(self, tag, priority):
		s = userTagJunction.update().\
			where(user_id=self.id, keyword_id=tag.id).\
			values(priority=priority)
		db.session.execute(s)
	def getTagPriority(self, tag):
		s = select([userTagJunction]).where(keyword_id=tag.id, user_id=self.id)
		result = db.session.execute(s)

		return result[0]["priority"]

	def savePost(self, post):
		self.saves.append(post)
		db.session.commit()

	def ratePost(self, post, rating):
		try:
			s =	userPostInteraction.update().\
				where(user_id=self.id, post_id=post.post_id).\
				values(rating=rating)
			db.session.execute(s)
		except:
			#User has not yet saved the post so there is no entry here
			s =	userPostInteraction.insert().\
				values(save=False, rating=rating, user_id=self.id, post_id=post.post_id)
			db.session.execute(s)


#Junction Table relating Users and Tags
userTagJunction = db.Table('userTagJunction',
	db.Column('user_id', db.Integer,
		db.ForeignKey(User.id),primary_key = True) ,
	db.Column('keyword_id', db.Integer,db.ForeignKey(Tag.id) ,
		primary_key = True) ,
	db.Column('priority' , db.Enum(PriorityType), default=PriorityType.follow)
)

userPostInteraction = db.Table('userPostInteraction',
	db.Column('user_id', db.Integer,
		db.ForeignKey(User.id), primary_key=True),
	db.Column('post_id', db.Integer,
		db.ForeignKey(Post.post_id), primary_key=True),
	db.Column('rating', db.Integer, default=0),
	db.Column('save', db.Boolean, default=True)
)
