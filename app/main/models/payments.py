"""DB model for payments"""

from . import db
from app.mail.util.sendgrid import send_mail
class Payment(db.Model):
    """
    Description of Payment Model.
    Rows
    -----------
    :id: int [pk]
    :username: varchar [ref: > users.username, not null]
    :amount: float [not null]
    :api_response: text [not null]
    """
    pay_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), db.ForeignKey("user.username"), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    api_response = db.Column(db.Text)

    user = db.relationship('User', backref='payments')

    def __init__(self, user, amount, api_response):
        self.username = user.username
        self.amount = amount
        self.api_response = api_response

        send_mail(user.email, "Thanks from Ambit", """
We are very grateful to you. Blah Blah Blah.""")

    def total(self):
        all_pays = self.query.filter(username == self.username).fetchall()
        sum = 0
        for pay in all_pays:
            sum += pay.amount
        
