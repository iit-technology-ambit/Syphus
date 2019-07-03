"""DB Model for Tag and Junction Tables connecting to User and Post"""
from . import db
class Tag(db.Model):
    """Description of Tag Model
    Rows
    -------
    id int [pk]
    name varchar [not null]
    """
    #Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

tagPostJunction = db.Table('tagPostJunction',
                            db.Column('post_id', db.Integer,
                                      db.ForeignKey('post.post_id'),
                                      primary_key=True),
                            db.Column('tag_id', db.Integer,
                                      db.ForeignKey('tag.id'),
                                      primary_key=True)
)

#TODO: userPostJunction
