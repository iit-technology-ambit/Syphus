import datetime
from logging import getLogger

from app.main import db
from app.main.models.enums import Month

LOG = getLogger(__name__)

def convertDateString(publish_date):
    format_str = '%d-%m-%Y'
    datetime_object = datetime.datetime.strptime(publish_date, format_str)
    return datetime_object


class Newsletter(db.Model):
    """
    Description of Newsletter Model
    Rows
    ------------------------
    :id: int [pk]
    :description text
    :publish_date: varchar
    :newsletter_content: text
    :upload_time datetime
    :cover_image_url: varchar
    """

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.Text)
    publish_date = db.Column(db.String(255))
    newsletter_content = db.Column(db.Text)
    upload_time = db.Column(db.DateTime)
    cover_image_url = db.Column(db.String(255))

    def __init__(self, description, publish_date, newsletter_content, cover_image_url):
        try:
            self.description = description
            self.publish_date = publish_date
            self.newsletter_content = newsletter_content
            self.upload_time = convertDateString(publish_date)
            self.cover_image_url = cover_image_url
            db.session.add(self)
            db.session.commit()

            LOG.info("New Newsletter Created - {}".format(publish_date))
        except BaseException:
            LOG.error("Cannot create Newsletter", exc_info=True)