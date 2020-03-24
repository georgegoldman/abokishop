import os
import secrets
from flask import Blueprint, redirect, url_for, flash, Markup, request, render_template, jsonify, make_response
from flask_login import login_required, current_user
from .web_forms import CreateShop, UpdateAccountInfo, AddStock
from .models import Shop, User, Goods, Notification, Order
from . import db, app, pusher_client
from werkzeug import secure_filename
from . import ALLOWED_EXTENSIONS

def allowed_file(filename):
    return '.' in filename and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

op = Blueprint('op', __name__)


@op.route('/update_profile', methods=['GET','POST'])
@login_required
def update_user_profile():
    form = UpdateAccountInfo()
    if form.validate_on_submit():
        f_name = form.first_name.data
        l_name = form.last_name.data
        email = form.email.data
        image = request.files['image']
        filename = ''
        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            random_hex = secrets.token_hex(8)
            _, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], picture_fn))
            current_user.image_file = picture_fn
            current_user.first_name = f_name
            current_user.last_name = l_name
            current_user.email = email
            db.session.commit()
            return redirect(url_for('view.user_account_info'))
        if form.errors:
            flash(form.errors, 'danger')
            return render_template('user_account_info.html', form=form)

@op.route('/addstock', methods=['POST'])
@login_required
def add_stock():
    form = AddStock()
    owner = request.args.get('shop_name')
    if form.validate_on_submit():
        stock_name = form.goods_name.data
        description = form.description.data
        price = form.price.data
        shop_id = int(request.args.get('shop_id'))
        goods = Goods(goods_name=stock_name, description=description, price=price, shop_id=shop_id)
        db.session.add(goods)
        db.session.commit()
        return redirect(url_for('view.in_shop', owner=owner))
    else:
        return redirect(url_for('view.in_shop', owner=owner))

@op.route('/booking')
def notify():
    user = request.args.get('user')
    stock = request.args.get('stock')
    goods_id = request.args.get('goods_id')
    owner = request.args.get('shop_name')
    info = f'{user} booked for {stock}'
    order = Order.query.filter_by(stock_ordered=stock).filter_by(customer=user).first()
    message = f'{current_user.last_name} you just booked for {stock} services'
    if order:
        order.amount += 1
        db.session.commit()
        info = f'{user} booked for {stock}'
        notify = Notification(info=info, notifier=order.goods.shop.shop_owner.last_name, order_id=order.id)
        db.session.add(notify)
        db.session.commit()
        pusher_client.trigger('notify-channel', 'new-notification', {'msg': message})
        return redirect(url_for('view.in_shop', owner=owner))

    order = Order(stock_ordered=stock, customer=user, amount=1, stock_id=goods_id)
    db.session.add(order)
    db.session.commit()
    notify = Notification(info=info, notifier=order.goods.shop.shop_owner.last_name, order_id=order.id)
    db.session.add(notify)
    db.session.commit()
    pusher_client.trigger('notify-channel', 'new-notification', {'msg': message})
    return redirect(url_for('view.in_shop', owner=owner))