import geocoder
from flask import Blueprint, render_template, request, request, jsonify
from .web_forms import SignupForm, LoginForm, CreateShop
from flask_login import login_required, current_user
from .models import Shop

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


@view.route('/market')
@login_required
def market():
    shops = Shop.query.all()
    
    return render_template('market.html', shops=shops)

@view.route('/store')
@login_required
def store():
    return render_template('store.html')


@view.route('/create_shop_form')
def create_shop_form():

    user_id = request.args.get('user_id')
    form = CreateShop()
    return render_template('create_shop.html', form=form, user_id=user_id)