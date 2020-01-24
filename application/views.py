import os
import geocoder
from flask import Blueprint, render_template, request, request, jsonify, url_for, redirect
from .web_forms import SignupForm, LoginForm, CreateShop, UpdateAccountInfo, PostGoodsForm
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

@view.route('/create_shop', methods=['POST'])
def create_shop():
    signup_form  = SignupForm()
    if signup_form.validate_on_submit():
        u_info = {
            'first_name': f'{signup_form.first_name.data}',
            'last_name':f'{signup_form.last_name.data}',
            'shop_name':f'{signup_form.shop_name.data}',
            'password':f'{signup_form.password.data}'
        }
        return render_template('create_shop.html', form=CreateShop(), u_info=u_info)
    return render_template('signup.html', form=signup_form)


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
    return render_template('store.html', current_user=current_user,)

@view.route('/in_shop')
@login_required
def in_shop():
    form = PostGoodsForm()
    shop_id = request.args.get('shop_id')
    shop  = Shop.query.get(int(shop_id))
    image_file = url_for('static', filename = 'imgs/profile_imgs/'+current_user.image_file)
    return render_template('in_shop.html', current_user=current_user, shop=shop, image_file=image_file, form=form)

@view.route('/user_account_info')
@login_required
def user_account_info():
    form = UpdateAccountInfo()
    image_file = url_for('static', filename = 'imgs/profile_imgs/'+current_user.image_file)
    return render_template('user_account_info.html', current_user=current_user, image_file=image_file, form=form)
