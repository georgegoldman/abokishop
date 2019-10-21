from flask import Blueprint, render_template
from .web_forms import SignupForm, LoginForm
from flask_login import login_required, current_user

view = Blueprint('view', __name__)

@view.route('/')
def abokishop():
    return render_template('basic-nav.html', current_user=current_user)

@view.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', form=form)

@view.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@view.route('/home')
@login_required
def home():
    return render_template('home.html')
