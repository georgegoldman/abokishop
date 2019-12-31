from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from wtforms.validators import  Length, EqualTo, ValidationError, DataRequired, Email, InputRequired
from .models import Shop

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

class CreateShop(FlaskForm):
    shop_name = TextField('Shop name', validators=[InputRequired(message='Name required')])
    service= SelectField(
        u'enter choice of service',
        choices=[
            (None,'None'),
            ('Automotive', 'Automotive'),
            ('Beauty,Spa & Salon', 'Beauty,Spa & Salon'),
            ('Building & Construction', 'Building & Construction'),
            ('Clothing & Apparel', 'Clothing & Apparel'),
            ('Education', 'Education'),
            ('Entertainment', 'Entertainment'),
            ('Event Planning & Services', 'Event Planning & Services'),
            ('Finance & Banking', 'Finance & Banking'),
            ('Food & Grocery', 'Food & Grocery'),
            ('Hotel & Lodging', 'Hotel & Lodging'),
            ('Medical Health', 'Medical Health'),
            ('Non-Profit', 'Non-Profit'),
            ('Professional Services', 'Professional Services'),
            ('Public Services', 'Public Services'),
            ('Restaurant', 'Restaurant'),
            ('Shopping & Retail', 'Shopping & Retail'),
            ('Travel & Transport', 'Travel & Transport'),
            ('others', 'others')
        ],
        validators=[InputRequired(message='you must make a selection')]
    )
    service_description = StringField(u'Enter shop description', widget=TextArea())

    create = SubmitField('create')