# for login/logout operations

from app.main.models.users import User
from flask_login import current_user, login_user, logout_user
from logging import getLogger

LOG = getLogger(__name__)


class Authentication:

	@staticmethod
	def login_user(data):
		try:
			if current_user.is_authenticated:
				response_object = {
					'status': 'Invalid' ,
					'message': 'Already Logged In' ,
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
					'message': 'email or password does not match.' ,
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
					'status' : 'Invalid',
					'message' : 'Not logged in',
				}
				return response_object, 300
			logout_user()
			response_object = {
				'status': 'Success',
				'message': 'Logged Out Successfully' ,
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
