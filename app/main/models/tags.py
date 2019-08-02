"""DB Model for Tag"""
from logging import getLogger

from app.main import db

LOG = getLogger(__name__)


class Tag(db.Model):
    """
    Description of Tag Model
    Rows
    -------
    :id: int [pk]
    :name: varchar [not null]
    """
    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    def __init__(self, name):
        """
        Params
        -----------
        :name: Name of the tag
        """
        self.name = name
        LOG.info("Adding new tag: %s", self.name)
        db.session.add(self)
        db.session.commit()

    def delete(self):
        LOG.info("Deleting tag: %s", self.name)
        db.session.delete(self)
        db.session.commit()
