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
email = AuthDto.reset_email


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


# # Verify Email after signing up
# @api.route('/email_verification')
# class SendVerificationEmail(Resource):
#     """ Send user verification mail to the user."""
#     @api.doc('Endpoint for sending a verification mail to the user')
#     def post(self):
#         return Authentication.send_verification()


# Verify the Email Token
@api.route('/confirm/<token>', methods=['GET'])
class ConfirmToken(Resource):
    """ Confirm the Email Verification Token Sent """
    @api.doc('Endpoint to Confirm the Email Verification Token Sent ')
    def get(self, token):
        return Authentication.confirm_token_service(token)

# I think we can implement this without this function, remove if redundant


# Request a reset of Password


@api.route('/reset/request', methods=["POST"])
class ResetRequest(Resource):
    """Send a request to change the password """
    @api.doc('Endpoint to Send a request to change the password ')
    @api.expect(email, validate=True)
    def post(self):
        post_data = request.json
        return Authentication.reset_password_mail(data = post_data)


@api.route('/reset/<token>', methods=["GET", "POST"])
class ResetTokenVerify(Resource):
    """Confirm the token sent to change the password and set a new password."""
    @api.doc('Endpoint to Confirm the token sent to change the password and set a new password')
    def get(self, token):
        return Authentication.confirm_reset_token_service(token)
    
    def post(self, token):
        return Authentication.reset_password_with_token(token)
