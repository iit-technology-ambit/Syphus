"""DB Model for imgLink table"""
from . import *
# from app.main import db
from flask import current_app
import datetime
from logging import getLogger
import os
LOG = getLogger(__name__)

imgPostJunction = db.Table('imgPostJunction',
                           db.Column('img_id', db.Integer,
                                     db.ForeignKey('imgLink.id'),
                                     primary_key=True),
                           db.Column('post_id', db.Integer,
                                     db.ForeignKey('post.post_id'))
                           )


class ImgLink(db.Model):
    """
    Description of ImgLink Model
    Rows
    -----------
    :id: int [pk]
    :link: varchar (url)
    """
    __tablename__ = 'imgLink' 

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(256), nullable=False)

    def __init__(self, imageBinary):
        """
        Pass a binary image in imageBinary and it will be saved.
        Image Naming Convention: present utc timestamp.png
        [Needs to be changed]
        """
        fname = datetime.datetime.now() + ".png"
        file = open(os.path.join(current_app.config["IMGDIR"], fname), "wb")
        LOG.info("Writing new image to disk, %s", fname)
        file.write(imageBinary)
        file.close()

        self.link = os.path.join(current_app.config["IMGDIR"], fname)

        LOG.info("New imgLink added to database.")
        db.session.add(self)
        db.session.commit()

    def delete(self):
        LOG.info("Removing image from disk")
        os.remove(self.link)

        LOG.info("ImgLink deleted: %s", self.link)
        db.session.delete(self)
        db.session.commit()

    def update(self, newImgBin):
        id = self.id
        self.delete()

        self.id = id
        fname = datetime.datetime.now() + ".png"
        file = open(os.path.join(current_app.config["IMGDIR"], fname), "wb")
        LOG.info("Writing new image to disk, %s", fname)
        file.write(newImgBin)
        file.close()

        self.link = os.path.join(current_app.config["IMGDIR"], fname)

        LOG.info("New imgLink added to database.")
        db.session.add(self)
        db.session.commit()


