from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import  Length, EqualTo, ValidationError, DataRequired, Email, InputRequired

class SignupForm(FlaskForm):
    '''signup form'''

    email = EmailField('Email', validators=[DataRequired(message='Email required'), Email()])
    username = TextField('Username', validators=[DataRequired(message='Username required')])
    password = PasswordField('Password', validators=[DataRequired(message='Password required')])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(message='Confirm password required'), EqualTo('password', message='your passwords must match') ])
    submit = SubmitField('signup')

class LoginForm(FlaskForm):
    '''login form'''
    email = EmailField('Email', validators=[DataRequired(message='Email required'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password required')])
    submit = SubmitField('login')
