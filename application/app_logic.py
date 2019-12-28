from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required
from .web_forms import CreateShop
from .models import Shop

op = Blueprint('op', __name__)

@op.route('/create_shop', methods=['POST'])
def create_shop():


    try:    
        form  = CreateShop()

        if form.validate_on_submit():
            shop_name = form.shop_name.data
            service = form.service.data
            service_type = form.service_name.data

            shop = Shop(shop_name=shop_name, service=service, service_type=service_type)

            flash('Your shop is newly open for sales')
            return 'hello'

    except (AttributeError):

        flash('you did enter all necessary information about your new shop')
        return redirect(url_for('view.create_shop_form'))
    finally:
        return 'opps the server is not available'
