from flask_wtf import FlaskForm
from flask_wtf.html5 import NumberInput
from wtforms import StringField, PasswordField, SelectField, ValidationError, FileField, TextField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, EqualTo
from wtforms.fields.html5 import EmailField
from wtforms.fields import StringField
from wtforms.widgets import TextArea
from .location_list import list_of_country, list_of_services
from .models import Shop, User

import re

def is_proper_username(form, field):
    if not re.match(r" +^\w+$", field.data) and re.match(' +', field.data):
        msg = f'{field.name} should have any of these characters only: a-z0-9_'
        raise ValidationError(msg)

def validate_password(form, field):
    data = field.data
    if not re.findall('.*[a-z].*', data):
        msg = f'{field.name} should have at least one lowercase character'
        raise ValidationError(msg)
    # has at least one uppercase character
    if not re.findall('.*[A-Z].*', data):
        msg = f'{field.name} should have at least one uppercase character'
        raise ValidationError(msg)
    # has at least one number
    if not re.findall('.*[0-9].*', data):
        msg = f'{field.name} should have at least one number'
        raise ValidationError(msg)
    # has at least one special character

def validate_shop(form, field):
    shop = Shop.query.filter_by(name=field.data).first()
    if shop:
        raise ValidationError('this shop name is taken')

def validate_email(form, field):
    email = User.query.filter_by(email=field.data).first()
    if email:
        raise ValidationError('This email is already in use')


class SignupForm(FlaskForm):

    first_name  = StringField(validators=[InputRequired(message='First name required'), is_proper_username], render_kw={'placeholder':'first name'})
    last_name  = StringField(validators=[InputRequired(message='Last name required'), is_proper_username], render_kw={'placeholder':'Last name'})
    shop_name  = StringField(validators=[InputRequired(message='Shop name required'), validate_shop], render_kw={'placeholder':'Shop name'})
    password = PasswordField(validators=[InputRequired(message='password required'), validate_password], render_kw={'placeholder':'password'})
    confirm_password = PasswordField(validators=[InputRequired(message='password required'), validate_password, EqualTo('password', message='Passwords must match')], render_kw={'placeholder':'confirm'})

class LoginForm(FlaskForm):

    shop_name = StringField(validators=[InputRequired(message='First name required'), ], render_kw={'placeholder':'Shop name'})
    password = PasswordField(validators=[InputRequired(message='password required'), validate_password], render_kw={'placeholder':'password'})

class CreateShop(FlaskForm):

    email = EmailField(validators=[InputRequired(message='please enter a valid email account'), validate_email], render_kw={'placeholder':'Enter a valid email'})
    service = SelectField(choices=
        [(service,service)for service in list_of_services
    ], validators=[InputRequired()])
    services_description = StringField(widget=TextArea(), render_kw={'placeholder':'Throw a little light about you shop'}, validators=[InputRequired(message='An information about your shop is needed')])
    country = SelectField(choices=[
        (country,country)for country in list_of_country
    ], validators=[InputRequired()])
    state_or_province = StringField(render_kw={'placeholder':'State or Province, local govt Area'}, validators=[InputRequired()])
    town = StringField(render_kw={'placeholder':'Town, Bus stop'}, validators=[InputRequired()])
    street = StringField(render_kw={'placeholder':'Street'}, validators=[InputRequired()])

    def validate_service(self, service):
        if service.data == 'Select service':
            raise ValidationError('Please select a service')

    def validate_country(self, country):
        if country.data == 'Select country':
            raise ValidationError('Please select a country')

class UpdateAccountInfo(FlaskForm):
    first_name = StringField(render_kw={'placeholder':'Update first name', 'autofocus':'autofocus', 'class':'form-control'})
    last_name = StringField(render_kw={'placeholder':'Update last name', 'class':'form-control'})
    email = EmailField(render_kw={'placeholder':'Update email', 'class':'form-control'})
    image = FileField(render_kw={'class':'form-control col-lg-6'})

class PostGoodsForm(FlaskForm):
    goods_name = StringField(render_kw={'placeholder':'Goods or service name', 'class':'col-lg-6 mb-3 col-12 form-control'})
    description = TextAreaField(render_kw={'placeholder':'Service or goods description', 'class':'col-lg-6 mb-3 col-12 form-control'})
    price = IntegerField(widget=NumberInput(), validators=[InputRequired()], render_kw={'placeholder':'Enter Price','class':'col-lg-3 mb-3 col-12 form-control'})
