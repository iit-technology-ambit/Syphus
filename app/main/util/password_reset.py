from flask import current_app
from itsdangerous import URLSafeTimedSerializer


def generate_reset_token(email):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(
        email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

# valid for only an hour


def confirm_reset_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=current_app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except BaseException:
        return False
    return email
