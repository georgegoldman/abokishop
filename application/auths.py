from flask import Blueprint, flash, redirect, url_for, request, render_template, redirect
from flask_login import login_user, logout_user, login_required
from .web_forms import SignupForm, CreateShop, LoginForm, UpdateAccountInfo
from .models import User, Shop
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/create_account', methods=['POST'])
def make_shop():
    form = CreateShop()
    u_f_name = f"{request.args.get('f_name')}"
    u_l_name = f"{request.args.get('l_name')}"
    u_password = f"{request.args.get('password')}"
    s_name = f"{request.args.get('s_name')}"
    if form.validate_on_submit():
        # return 'is_authenticated'

        u_email = form.email.data
        service = form.service.data
        service_description = form.services_description.data
        country = form.country.data
        state_or_province = form.state_or_province.data
        town = form.town.data
        street = form.street.data
        user = User(first_name=u_f_name, last_name=u_l_name, email=u_email, password=generate_password_hash(u_password,method='sha256'))
        db.session.add(user)
        db.session.commit()
        new_user = User.query.filter_by(email=u_email).first()
        return redirect(ul_for('auth.build_shop', new_user_id=new_user.id, s_name=s_name, service=service, service_description=service_description, country=country, state_or_province=state_or_province, town=town, street=street))
    u_info = {
        'first_name': f'{u_f_name}',
        'last_name':f'{u_l_name}',
        'shop_name':f'{s_name}',
        'password':f'{u_password}'
    }
    return render_template('create_shop.html', form=form, u_info=u_info)

    # return redirect(url_for('view.create_shop'))
    # return f'{u_email}'

@auth.route('/build_shop')
def build_shop():
    new_user_id = request.args.get('new_user_id')
    to_int = int(new_user_id)
    # print(type(int(new_user_id)))
    # return new_user_id
    s_name = request.args.get('s_name')
    service = request.args.get('service')
    service_description = request.args.get('service_description')
    country = request.args.get('country')
    state_or_province = request.args.get('state_or_province')
    town = request.args.get('town')
    street = request.args.get('street')
    shop = Shop(name=s_name, service=service, service_description=service_description,country=country,state_or_province=state_or_province,town=town,street=street,owner=to_int)
    db.session.add(shop)
    db.session.commit()
    return redirect(url_for('view.login'))

@auth.route('/signin', methods=['POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        shop_name = form.shop_name.data
        password = form.password.data
        shop = Shop.query.filter_by(name=shop_name).first()
        if shop and check_password_hash(shop.shop_owner.password, password):
            name = shop.name
            login_user(shop.shop_owner)
            return redirect(url_for(f'view.market', shop_id=shop.id))
    flash('Please check your log details')
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.abokishop'))
