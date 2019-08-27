"""DB Model for imgLink table"""
import datetime
import os
from logging import getLogger

from flask import current_app
from werkzeug.utils import secure_filename

from app.main import db

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

    def __init__(self, image=None, link=None):
        """
        Pass a werzeug fileStorage in image and it will be saved.
        Image Naming Convention: present utc timestamp.png
        Or
        Just pass the link and it will add it to database
        """

        if image is not None:
            # LOG.info(image)
            fname = os.path.join(current_app.config["IMGDIR"],
                                 secure_filename(image.filename) +
                                 "_" + str(datetime.datetime.now()).replace(" ", "_"))

            LOG.info("Writing new image to disk, %s", fname)
            image.save(fname)

            self.link = fname

            LOG.info("New imgLink added to database.")
            db.session.add(self)
            db.session.commit()
        elif link is not None:
            self.link = link
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
