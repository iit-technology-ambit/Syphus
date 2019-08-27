"""
DB Model for the messages table
and the relationships connecting
messages and user
"""

import datetime

from app.main import db
from app.main.models.errors import LoginError
from app.main.models.users import User


class Message(db.Model):
    """
    Description of Messages model.
    Columns:
    -----------
    :message_id: int [pk]
    :sender_id: int [ref: > users.id]
    :receiver_id: int [ref: > users.id]
    :message: text
    :sent_at: timestamp [not null]
    """

    # Columns
    message_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(
        db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    sent_at = db.Column(
        db.DateTime, default=datetime.datetime.now(), nullable=False)

    # Relationships
    sender_id = db.relationship('User', backref='messages', lazy=False)
    receiver_id = db.relationship('User', backref='messages', lazy=False)

    # Getter and Setter to check if sender is logged in
    @property
    def sender_id(self):
        return self.sender_id

    @sender_id.setter
    def login_check(self, senderId):
        try:
            user = User.query.filter(id == senderId).fetchone()
            if user.last_logout is not None:
                raise LoginError
        except BaseException:
            # Handle case when sender isn't logged in
            pass
