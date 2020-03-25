import os
import pusher
from flask import Flask, Markup
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate  import Migrate, MigrateCommand
from flask_script import Manager
from flask_fontawesome import FontAwesome


app = Flask(__name__)

app.config['DEBUG']=1
app.config['SECRET_KEY']=os.environ.get('SECRET')
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')
# app.config['SECRET_KEY'] = 'negjrhi52452325'
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:password@localhost/abokishop'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/application/static/imgs/profile_imgs'

pusher_client = pusher.Pusher(
    app_id ='966379',
    key = 'e271cf7723747ff31222',
    secret='5d871e0afa95b96799bf',
    cluster='eu',
    ssl=True
)



fa = FontAwesome(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from application import models
db.create_all()

login_manager = LoginManager(app)
from application.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_manager.login_view = 'auth.login'
login_manager.login_message = Markup("Please login")


from application.views import view
app.register_blueprint(view)

from application.auths import auth
app.register_blueprint(auth)


from application.app_logic import op
app.register_blueprint(op)
