from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo


class PasswordForm(Form):
    password = PasswordField('Password', validators=[
        DataRequired(),
        EqualTo('confirmPassword', message="Passwords must match!")
    ])
    confirmPassword = PasswordField(
        'Repeat Password', validators=[DataRequired()])
