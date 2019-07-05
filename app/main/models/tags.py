"""DB Model for Tag"""
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

#TODO: userPostJunction
