import os
import secrets
from flask import Blueprint, redirect, url_for, flash, Markup, request, render_template
from flask_login import login_required, current_user
from .web_forms import CreateShop, UpdateAccountInfo, AddStock
from .models import Shop, User, Goods
from . import db, app
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
    if form.validate_on_submit():
        stock_name = form.goods_name.data
        description = form.description.data
        price = form.price.data
        shop_id = int(request.args.get('shop_id'))
        goods = Goods(goods_name=stock_name, description=description, price=price, shop_id=shop_id)
        db.session.add(goods)
        db.session.commit()
        return f' {stock_name} {description} {price} stocks are added!'