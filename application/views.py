import geocoder
from flask import Blueprint, render_template, request, request, jsonify
from .web_forms import SignupForm, LoginForm, CreateShop
from flask_login import login_required, current_user

view = Blueprint('view', __name__)

@view.route('/')
def abokishop():
    return render_template('welcome.html', current_user=current_user,)

@view.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)

@view.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@view.route('/home')
@login_required
def home():
    return render_template('home.html')

@view.route('/market')
def market():
    market_place = geocoder.ipinfo('me')
    
    return render_template('market.html', market_place=market_place)

@view.route('/store')
def store():
    return render_template('store.html')


@view.route('/create_shop_form')
def create_shop_form():

    form = CreateShop()
    return render_template('create_shop.html', form=form)