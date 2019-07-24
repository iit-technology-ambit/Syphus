'''
All Endpoints required for authentication
operations such as login, logout and signup. 
'''

from flask import request
from flask_restplus import Resource

from app.main.service.auth_service import Authentication
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
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
    pass

# Verify Email after signing up
@api.route('/email_verify')
class EmailVerify(Resource):
    pass


# Request a reset of Password
@api.route('/reset/request')
class ResetRequest(Resource):
    pass

# Reset Password
@api.route('/reset/<secure_token>')
class ResetTokenVerify(Resource):
    pass

