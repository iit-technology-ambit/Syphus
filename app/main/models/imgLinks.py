"""DB Model for imgLink table"""
from . import db

class ImgLink(db.Model):
    """Description of ImgLink Model
    Rows
    -----------
    id int [pk]
    link varchar (url)
    """
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=False)

imgPostJunction = db.Table('imgPostJunction',
                            db.Column('img_id', db.Integer,
                                      db.ForeignKey('imgLink.id'),
                                      primary_key=True),
                            db.Column('post_id', db.Integer,
                                      db.ForeignKey('post.id'))
)
