from itsdangerous import URLSafeTimedSerializer
from flask import current_app


def generate_reset_token(email):
	serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
	return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])


def confirm_reset_token(token, expiration=1800):
	serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
	try:
		email = serializer.loads(
			token,
			salt=current_app.config['SECURITY_PASSWORD_SALT'],
			max_age=expiration
		)
	except:
		return False
	return email
