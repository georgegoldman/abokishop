import os
import geocoder
from . import pusher_client
from flask import Blueprint, render_template, request, request, jsonify, url_for, redirect
from .web_forms import SignupForm, LoginForm, CreateShop, UpdateAccountInfo, AddStock
from flask_login import login_required, current_user
from .models import Shop, Notification, Goods, Order

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
    notification = Notification.query.all()
    notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
    return render_template('market.html', shops=shops, notification_ammount=notification_ammount)

@view.route('/store')
@login_required
def store():
    notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
    return render_template('store.html', current_user=current_user, notification_ammount=notification_ammount)


@view.route('/<string:owner>/home')
@login_required
def in_shop(owner):
    form = AddStock()
    # print(shop_id)
    shop  = Shop.query.filter_by(name=owner).first()
    image_file = url_for('static', filename = 'imgs/profile_imgs/'+current_user.image_file)
    # pusher_client.trigger('my-channel', 'my-event', {'message': 'the pusher is working'})
    try:
        # order = Order.query.filter_by(stock_id=shop).filter_by()
        notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
        notification = Notification.query.all()
        return render_template('in_shop.html' , current_user=current_user, shop=shop, image_file=image_file, form=form, notification=notification, notification_ammount=notification_ammount)
    except:
        return render_template('in_shop.html' , current_user=current_user, shop=shop, image_file=image_file, form=form,)

@view.route('/user_account_info')
@login_required
def user_account_info():
    form = UpdateAccountInfo()
    image_file = url_for('static', filename = 'imgs/profile_imgs/'+current_user.image_file)
    notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
    return render_template('user_account_info.html', current_user=current_user, image_file=image_file, form=form, notification_ammount=notification_ammount)

@view.route('/transaction')
@login_required
def transaction():
    order = Order.query.all()
    notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
    return render_template('transactions.html', order=order, notification_ammount=notification_ammount)#

@view.route('/notify')
@login_required
def notify():
    order = Order.query.all()
    notification_ammount = Notification.query.filter_by(read=False).filter_by(notifier=current_user.email).count()
    return render_template('notify.html',  order=order, notification_ammount=notification_ammount)