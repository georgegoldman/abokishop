import os
from flask import Flask, Markup
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['DEBUG']=1
app.config["GEOIPIFY_API_KEY"] = "8.8.8.8"
app.config['SECRET_KEY']=os.environ.get('SECRET')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
# app.config['SECRET_KEY'] = 'negjrhi52452325'
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/abokishop'


db = SQLAlchemy(app)

from application import models
db.create_all()

login_manager = LoginManager(app)
from application.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view = 'auth.login'
login_manager.login_message = Markup("hello please can you login or <a href='/signup' class='alert-link'>signup</a> up thanks")


from application.views import view
app.register_blueprint(view)

from application.auths import auth
app.register_blueprint(auth)
