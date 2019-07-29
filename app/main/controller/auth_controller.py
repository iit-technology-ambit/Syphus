'''
All Endpoints required for authentication
operations such as login, logout and signup. 
'''

from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Authentication
from app.main.util.dto import AuthDto, UserDto

api = AuthDto.api
user_auth = AuthDto.user_auth
user = UserDto.user


@api.route('/login')
class UserLogin(Resource):
    """ User Login Resource """
    @api.doc('Endpoint for User Login')
    @api.expect(user_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return Authentication.login_user(data=post_data)


@api.route('/logout')
class UserLogout(Resource):
    """
    Logout Resource
    """
    @api.doc('Endpoint for User Logout')
    def post(self):
        return Authentication.logout_user()


# Signup
@api.route('/signup')
class SignUp(Resource):

    @api.doc('Endpoint for Signing Up a new user')
    @api.expect(user, validate=True)
    def post(self):
        post_data = request.json
        return Authentication.signup_user(data=post_data)


# Verify Email after signing up
@api.route('/email_verification')
class SendVerificationEmail(Resource):
    """ Send user verification mail to the user."""
    @api.doc('Endpoint for sending a verification mail to the user')
    def post(self):
        post_data = request.json
        return Authentication.send_verification(data=post_data)


# Verify the Email Token
@api.route('/confirm/<token>')
class ConfirmToken(Resource):
    """ Confirm the Email Verification Token Sent """
    @api.doc('Endpoint to Confirm the Email Verification Token Sent ')
    def post(self, token):
        return Authentication.confirm_token(data=token)

# I think we can implement this without this function, remove if redundant


@api.route('/resend_email_verification')
class ResendVerificationEmail(Resource):
    """ Resend the Verification Email """
    @api.doc('Endpoint to resend the verification email')
    def post(self):
        post_data = request.json
        return Authentication.send_verification(data=post_data)

# Request a reset of Password


@api.route('/reset/request', methods=["GET", "POST"])
class ResetRequest(Resource):
    """ Send a request to change the password """
    @api.doc('Endpoint to Send a request to change the password ')
    def post(self):
        post_data = request.json
        return Authentication.reset_password_mail(data = post_data)


@api.route('/reset/<token>', methods=["GET", "POST"])
class ResetTokenVerify(Resource):
    """ Confirm the token sent to change the password and set a new password """
    @api.doc('Endpoint to Confirm the token sent to change the password and set a new password')
    def post(self, token):
        return Authentication.confirm_reset_token(data=token)
