from app.main.config import sendgrid_key, from_mail
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from logging import getLogger
from process import make_async


LOG = getLogger(__name__)


@make_async
def send_mail(to_mail, mail_subject, mail_body):
	"""
	Function to send a mail using Sendgrid API

    Parameters:
    arg1 (string): The recipient's email address.
    arg2 (string): The subject of the mail.
    arg3 (string): The body of the mail.

    """


    message = Mail(
        from_email=from_mail,
        to_emails=to_mail,
        subject=mail_subject,
        html_content=mail_body)

    try:
        sg = SendGridAPIClient(sendgrid_key)
        response = sg.send(message)
        LOG.debug("Mail to {} regarding {} successful".format(to_mail, mail_subject))
        LOG.debug(response.status_code)
       	LOG.debug(response.body)
        LOG.debug(response.headers)
    except Exception as e:
    	LOG.error("Mail to {} regarding {} failed. ".format(to_mail, mail_subject))
        LOG.error(str(e))
