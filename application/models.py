from datetime import datetime
from application import db
from flask_login import UserMixin, current_user

class User(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    email = db.Column(db.Text)
    image_file = db.Column(db.Text, default='default.jpg')
    password = db.Column(db.Text)
    shop = db.relationship('Shop', backref='shop_owner', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'[{self.id}, {self.first_name}]'

class Shop(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    service = db.Column(db.Text)
    service_description = db.Column(db.Text)
    country = db.Column(db.Text)
    state_or_province = db.Column(db.Text)
    town = db.Column(db.Text)
    street = db.Column(db.Text)
    owner = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goods = db.relationship('Goods', backref='shop', lazy=True)

    def __init__(self, name, service, service_description, country, state_or_province, town, street, owner):
        self.name = name
        self.service = service
        self.service_description = service_description
        self.country = country
        self.state_or_province = state_or_province
        self.town = town
        self.street = street
        self.owner = owner


    def __repr__(self):
        return f'[{self.name}, {self.service}, {self.service_description}]'

class Goods(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    goods_name = db.Column(db.Text)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    shop_id = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)
    order = db.relationship('Order', backref='goods', lazy=True)



    def __init__(self, goods_name, description, price, shop_id):
        self.goods_name = goods_name
        self.description = description
        self.price = price
        self.shop_id = shop_id

    def __repr__(self):
        return f'[{self.goods_name}, {self.description}, {self.price}]'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_ordered = db.Column(db.Text)
    customer = db.Column(db.Text)
    amount = db.Column(db.Integer)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    stock_id = db.Column(db.Integer, db.ForeignKey('goods.id'), nullable=False)
    notification = db.relationship('Notification', backref='order', lazy=True)

    def __init__(self, stock_ordered, customer, amount, stock_id):
        self.stock_ordered = stock_ordered
        self.customer = customer
        self.amount = amount
        self.stock_id = stock_id

    def __repr__(self):
        return f'[{self.stock_ordered}, {self.customer}, {self.amount}, {self.time}, {self.stock_id}]'

class Notification(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.Text)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    notifier = db.Column(db.Text)
    read = db.Column(db.Boolean, default=False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)


    def __init__(self, info, order_id, notifier):
        self.info = info
        self.order_id = order_id
        self.notifier  = notifier

    def __repr__(self):
        return f'[{self.info}, {self.stock_id}]'
