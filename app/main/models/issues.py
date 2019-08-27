import datetime
from logging import getLogger

from app.main import db
from app.main.models.enums import Month
from app.main.models.tags import Tag

LOG = getLogger(__name__)


class Issue(db.Model):
    """
    Description of Issue Model
    Rows
    ------------------------
    :id: int [pk]
    :date_created: datetime
    :month: Month
    :year: int
    :issue_tag: varchar [ref: > tags.name]
    :cover: int [ref: > imgLinks.id]
    :link: varchar
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    created_at = db.Column(db.DateTime)
    month = db.Column(db.Enum(Month))
    year = db.Column(db.Integer)
    issue_tag = db.Column(db.String(20), db.ForeignKey('tag.name'))
    cover = db.Column(db.Integer, db.ForeignKey('imgLink.id'))
    link = db.Column(db.String(256))
    description = db.Column(db.Text, nullable=True)

    tag = db.relationship('Tag', lazy=False)
    cover_img = db.relationship('ImgLink', lazy=False)

    def __init__(self, coverId, month, year, link):
        try:
            tagName = str(month) + str(year[-2:])
            self.created_at = datetime.datetime.now()
            self.month = Month[month]
            self.year = year
            self.link = link
            self.cover = coverId

            self.setIssueTag(tagName)
            db.session.add(self)
            db.session.commit()

            LOG.info("New Issue Created")
        except BaseException:
            LOG.error("Cannot create Issue", exc_info=True)

    def setIssueTag(self, tagName):
        existing_tags = Tag.query.filter_by(name=tagName).all()
        if len(existing_tags) == 0:
            existing_tag = Tag(tagName)
            self.tag = existing_tag
            db.session.commit()
        else:
            self.tag = existing_tags[0]
            db.session.commit()

        LOG.info(f"Issue tag set for { tagName }")

    def setDescription(self, desc):
        self.description = desc
        db.session.commit()
