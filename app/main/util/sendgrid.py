from logging import getLogger

from flask import Flask, current_app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from app.main.util.process import make_async

app = Flask(__name__)
LOG = getLogger(__name__)


@make_async
def async_send_mail(app, to_mail, mail_subject, mail_body):
    with app.app_context():
        send_mail(to_mail, mail_subject, mail_body)


@make_async
def async_subscribe(app, email):
    with app.app_context():
        subscribe_newsletter(email)


def send_mail(to_mail, mail_subject, mail_body):
    """
    Function to send a mail using Sendgrid API

    Parameters:
    arg1 (string): The recipient's email address.
    arg2 (string): The subject of the mail.
    arg3 (string): The body of the mail.

    """

    message = Mail(
        from_email=current_app.config['FROM_MAIL'],
        to_emails=to_mail,
        subject=mail_subject,
        html_content=mail_body)

    try:
        sg = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
        response = sg.send(message)
        LOG.info("Mail to {} regarding {} successful".format(
            to_mail, mail_subject))
        LOG.info(response.status_code)
        LOG.info(response.body)
        LOG.info(response.headers)
    except Exception as e:
        LOG.error("Mail to {} regarding {} failed. ".format(
            to_mail, mail_subject), exc_info=True)


def subscribe_newsletter(email):
    """
    Add subscriber to the newsletter contact list.

    :param email: email address
    :return: None
    """
    # id of the newsletter_subs list
    list_id = '3553b851-9c85-4190-9110-06b32a6158c7'
    data = [
        {
            "email": email.lower()
        }
    ]
    try:
        sg = SendGridAPIClient(current_app.config['SENDGRID_API_KEY'])
        response = sg.client.marketing.contacts.put(request_body={
            "list_ids": [list_id],
            "contacts": data
        })
        print(str(response.body))
    except Exception as e:
        LOG.error("Adding subscriber {} to newsletter failed".format(
            email), exc_info=True)
