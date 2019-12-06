from flask import Blueprint, render_template, flash, redirect, url_for, Markup
from flask_login import login_user, logout_user, login_required
from .web_forms import SignupForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup():

    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user:
            flash(f"Account alredy exist")
            return redirect(url_for('view.login'))

        else:
            user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
            db.session.add(user)
            db.session.commit()
            flash('Account created')
            return redirect(url_for('view.login'))

    return render_template('signup.html', form=form)

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
            flash('invalid credentials  or you probably don\'t have an account')
            return redirect(url_for('view.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('view.abokishop'))
