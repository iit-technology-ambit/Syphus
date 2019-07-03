# DB Models for users goes here
from .. import db, flask_bcrypt

class User(db.Model):
	""" User Model for storing user related details """
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(255), unique=True,nullable=False)
	password_hash = db.Column(db.String(100))
	first_name=db.Column(db.String(255))
	last_name=db.Column(db.String(255))
	dob=db.Column(db.DateTime)
	email = db.Column(db.String(255), unique=True)
	fb_handle=db.Column(db.String(255),unique=True)
	g_handle=db.Column(db.String(255),unique=True)
	medium_handle=db.Column(db.String(255),unique=True)   
	profile_picture=db.Column(db.Integer,db.ForeignKey("imgLinks.id"))
	profile_picture=db.relationship("imgLinks") 
	

	@property
	def password(self):
		raise AttributeError('password: write-only field')

	@password.setter
	def password(self, password):
		self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

	def check_password(self, password):
		return flask_bcrypt.check_password_hash(self.password_hash, password)

	def __repr__(self):
		return "<User '{}'>".format(self.username)

class imgLinks(db.Model):
	id=db.Column(db.Integer,primary_key=True)

