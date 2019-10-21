from application import db
from flask_login import UserMixin

class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    stock_post = db.relationship('StockPost', backref='user', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'< User {self.id}>'

class StockPost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    about = db.Column(db.Text)
    cost = db.Column(db.Integer)
    user_id  = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, about, cost, user_id):
        self.name = name
        self.about = about
        self.cost = cost
        self.user_id = user_id


    def __repr__(self):
        return f'< StockPost {self.id}>'
