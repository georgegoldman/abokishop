from flask import Blueprint, flash, redirect, url_for, Markup, request
from flask_login import login_user, logout_user, login_required
from .web_forms import SignupForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .user_query import QU, QS

auth = Blueprint('auth', __name__)

def q_u_e(eml):
    return User.query.filter_by(email=eml).first()

@auth.route('/signup', methods=['POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = QU(email).em()
        if user:
            flash(f"Account alredy exist")
            return redirect(url_for('view.login'))
        else:
            user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(user)
            db.session.commit()
            user_id = QU(email).idt()
            flash(Markup(f"Account created, create a shop or <form method='POST' action='/login?email={email}' class='alert-link'><button class='btn btn-primary'>login</button></form>"))
            return redirect(url_for('view.create_shop_form', user_id=user_id))
            # return redirect(url_for('view.signup'))


@auth.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('view.home'))
        else:
            flash('Unable to verify')
            return redirect(url_for('view.login'))
    else:
        email  = request.args.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            login_user(user)
            return redirect(url_for('view.home'))

@auth.route('/login_acs')
def login_acs():
    user_id = request.args.get('user_id')

    return user_id
    # user = QU(int(user_id)).em()
    # login_user(user)
    # return redirect(url_for('view.home'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.abokishop'))
