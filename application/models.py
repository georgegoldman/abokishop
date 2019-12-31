from datetime import datetime
from application import db
from flask_login import UserMixin, current_user
from .location import Geolocation

class User(db.Model,UserMixin, Geolocation):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)
    shop = db.relationship('Shop', backref='shop', lazy='dynamic')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'[{self.id}, {self.username}]'

class Shop(db.Model, Geolocation):

    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.Text)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'))
    goods = db.relationship('Goods', backref='goods', lazy='dynamic')
    service = db.Column(db.Text)
    service_description = db.Column(db.Text)

    def __init__(self, shop_name, owner, service, service_description):
        self.shop_name = shop_name
        self.owner = owner
        self.service = service
        self.service_description = service_description


    def __repr__(self):
        return f'[{self.shop_name}, {self.service}, {self.service_description}]'

class Goods(db.Model, Geolocation):

    id = db.Column(db.Integer, primary_key=True)
    goods_name = db.Column(db.Text)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)



    def __init__(self, goods_name, description, price):
        self.goods_name = goods_name
        self.description = description
        self.price = price

    def __repr__(self):
        return f'[{self.goods_name}, {self.description}, {self.price}]'




