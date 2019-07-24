'''
DB Model for imgLink table
'''
from app.main import db

class ImgLink(db.Model):
    """
    Description of ImgLink Model
    Rows
    -----------
    :id: int [pk]
    :link: varchar (url)
    """
    __tablename__ = "imgLink"
    img_id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=False)

imgPostJunction = db.Table('imgPostJunction',
                            db.Column('img_id', db.Integer,
                                      db.ForeignKey('imgLink.img_id'),
                                      primary_key=True),
                            db.Column('post_id', db.Integer,
                                      db.ForeignKey('post.post_id'))
)
