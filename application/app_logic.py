from flask import Blueprint, redirect, url_for, flash, Markup, request
from flask_login import login_required, current_user
from .web_forms import CreateShop
from .models import Shop, User
from . import db
from .user_query import QS, QU

op = Blueprint('op', __name__)

@op.route('/create_shop', methods=['POST','GET'])
def create_shop():
    form  = CreateShop()
    if form.validate_on_submit():
        user_id = request.args.get('user_id')
        shop_name = form.shop_name.data
        service = form.service.data
        service_description = form.service_description.data
        shop  = Shop.query.filter_by(shop_name=shop_name).first()
        if shop:
            flash('Shop already exit choose another name')
            return redirect(url_for('view.create_shop_form'))
        else:
            user=QU(int(user_id)).em()
            new_shop = Shop(shop_name=shop_name, owner=user.id, service=service, service_description=service_description)
            db.session.add(new_shop)
            db.session.commit()

            return redirect(url_for('auth.login_acs', user_id=user.id))

        return Markup(f'shop name: {shop_name} <br> service: {service} <br> service decription: {service_description}')