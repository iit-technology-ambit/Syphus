'''
All Endpoints required for authentication
operations such as login, logout and signup. 
'''

from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Authentication
from ..util.dto import AuthDto, UserDto

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
@api.route('/email_verify')
class SendVerificationEmail(Resource):
     """ Send user verification mail to the user."""
     @api.doc('Endpoint for sending a verification mail to the user')
     def post(self):
        post_data = request.json
        return Authentication.send_verification(data=post_data)
        

#Verify the Email Token
@api.route('/confirm/<token>')
class ConfirmToken(Resource):
    """ Confirm the Email Verification Token Sent """
    def post(self,token):
        return Authentication.confirm_token(data=token)


# Request a reset of Password
@api.route('/reset/request')
class ResetRequest(Resource):
    """ Send a request to change the password """
    

# Reset Password


@api.route('/reset/<secure_token>')
class ResetTokenVerify(Resource):
    """ Confirm the token sent to change the password and set a new password """
    pass
