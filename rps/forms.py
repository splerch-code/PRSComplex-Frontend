from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, PasswordField
from wtforms.validators import Length, DataRequired, ValidationError, Email, EqualTo
from rps.models import User


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=4, max=64), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=2, max=64), DataRequired()])
    submit = SubmitField(label='Login')


class NewAccountForm(FlaskForm):
    username = StringField(label='Username:',
                           validators=[Length(min=4, max=64), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:',
                             validators=[Length(min=2, max=64), DataRequired(),
                                         EqualTo('password_confirm', 'Passwords must match')])
    password_confirm = PasswordField(label='Confirm Password:')
    create_account = SubmitField(label='Create New Account')
