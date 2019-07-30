# for login/logout operations
import traceback
from app.main.models.users import User
from app.main.util.sendgrid import async_send_mail
from app.main.util.email_verification import generate_confirmation_token, confirm_token
from app.main.util.password_reset import generate_reset_token, confirm_reset_token
from app.main.util.forms import PasswordForm
from flask import url_for
from flask import current_app as app
from flask_login import current_user, login_user, logout_user
from logging import getLogger

LOG = getLogger(__name__)


class Authentication:

    @staticmethod
    def login_user(data):
        try:
            if current_user.is_authenticated:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Already Logged In',
                }
                return response_object, 300
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                login_user(user, remember=data.get('remember'))
                response_object = {
                    'status': 'Success',
                    'message': 'Successfully logged in.',
                }
                return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.',
                }
                return response_object, 401

        except Exception as e:
            LOG.error('Login Failed')
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def logout_user(data):
        try:
            if not current_user.is_authenticated:
                response_object = {
                    'status': 'Invalid',
                    'message': 'Not logged in',
                }
                return response_object, 300
            logout_user()
            response_object = {
                'status': 'Success',
                'message': 'Logged Out Successfully',
            }
            return response_object, 200
        except Exception as e:
            LOG.error('Logout Failed')
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def signup_user(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user is not None:
                response_object = {
                    'status': 'Invalid',
                    'message': 'User Already Exists',
                }
                LOG.info(
                    'User already present in database. Redirect to Login Page')
                return response_object, 300

            user = User(data.get('id'), data.get('username'),
                        data.get('password'), data.get('email'))
            response_object = {
                'status': 'Success',
                'message': 'User added Successfully',
            }
            return response_object, 300

        except Exception as e:
            LOG.error('User with email {} couldn\'t be Signed Up. Please try again'.format(
                data.get('email')))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def send_verification():
        try:
            user = User.query.filter_by(email=current_user.email).first()
            if user.isVerified():
                response_object = {
                    'status': 'Invalid',
                    'message': 'Email is already Verified.',
                }
                return response_object, 300

            token = generate_confirmation_token(current_user.email)
            subject = "Hola! To hop onto IIT Tech Ambit, please confirm your email."
            confirm_url = url_for('api.auth_confirm_token',
                                  token=token, _external=True)
            async_send_mail(current_user.email, subject, confirm_url)

        except:
            LOG.error('Verification Mail couldn\'t be sent to {}. Please try again'.format(current_user.email))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def confirm_token(data):
        try:
            email = confirm_token(token)
        except:
            LOG.info('The confirmation link has expired or is invalid')
            response_object = {
                'status': 'Fail',
                'message': 'Verification link is invalid or has expired',
            }
            return response_object, 400

        user = User.query.filter_by(email=email).first()
        user.setVerified()
        response_object = {
            'status': 'Success',
            'message': 'Email Verified Successfully',
        }
        return response_object, 200

    @staticmethod
    def reset_password_mail(data):
        try:
            user = User.query.filter_by(email=data.get('email')).first()
            if user is None:
                LOG.info('User with email {} isn\'t registered.'.format(
                    data.get('email')))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User isn\'t registered. Please sign up first.',
                }
                return response_object, 300

            if user.isVerified() == False:
                LOG.info('Can\'t reset password since user email {} isn\'t verified.'.format(
                    data.get('email')))
                response_object = {
                    'status': 'Fail',
                    'message': 'User is not verified. Didn\'t send verification email.',
                }
                return response_object, 300

            reset_token = generate_reset_token(data.get('email'))
            subject = "Ah, Dementia! Here's a link to reset your password"
            reset_url = url_for('ResetTokenVerify.post',
                                token=token, _external=True)
            async_send_mail(data.get('email'), subject, reset_url)

        except:
            LOG.error('Verification Mail couldn\'t be sent to {}. Please try again'.format(
                data.get('email')))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def confirm_reset_token(data):
        try:
            email = confirm_reset_token(token)
        except:
            LOG.info('The password reset link has expired or is invalid')
            response_object = {
                'status': 'Fail',
                'message': 'Password Reset link is invalid or has expired',
            }
            return response_object, 400

        form = PasswordForm()

        if form.validate_on_submit():
        	user = User.query.filter_by(email=email).first()
        	user.resetPassword(form.password.data)
