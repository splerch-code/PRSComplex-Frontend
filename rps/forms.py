from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField, PasswordField
from wtforms.validators import Length, DataRequired, ValidationError, Email, EqualTo
from rps.models import User


class LoginForm(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=4, max=64), DataRequired()])
    password = PasswordField(label='Password:', validators=[Length(min=2, max=64), DataRequired()])
    submit = SubmitField(label='Login')


class NewAccountForm(FlaskForm):
    def validate_username(self, input_username):
        if User.query.filter_by(username=input_username.data.lower()).first():
            raise ValidationError('Account already created with email')

    def validate_email(self, input_email):
        if User.query.filter_by(username=input_email.data.lower()).first():
            raise ValidationError('Account already created with email')

    username = StringField(label='Username:',
                           validators=[Length(min=4, max=64), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    password = PasswordField(label='Password:',
                             validators=[Length(min=2, max=64), DataRequired(),
                                         EqualTo('password_confirm', 'Passwords must match')])
    password_confirm = PasswordField(label='Confirm Password:')
    create_account = SubmitField(label='Create New Account')
