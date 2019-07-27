from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class PasswordForm(Form):
    password = PasswordField('Password', validators=[DataRequired()])