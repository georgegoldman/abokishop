from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.fields.html5 import EmailField
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
    '''create shop'''

    shop_name = TextField('Shop name', validators=[DataRequired(message='shop name required')])
    service = SelectField(
        u'Service type',
        choices=[(None,None),('Services for people','Services for people' ), ('Services for goods', 'Services for goods')], 
        validators=[DataRequired(message='A service must be selected')]
    )
    service_name = TextField('Type of services', validators=[DataRequired(message='service_name')])
    create = SubmitField('Create Shop')

    def validate_service(self, service):
        if service.data == None:
            raise ValidationError('Please selecte a service')

    def validate_shop_name(self, shop_name):
        shop = Shop.query.filter_by(shop_name=shop_name.data).first()
        if shop:
            raise ValidationError('Shop name already taken')