from .models import User, Shop

class QU():
    def __init__(self,eml):
        self.eml = eml

    def em(self):
        if type(self.eml) == int:
            return User.query.get(self.eml)
        else:
            return User.query.filter_by(email=self.eml).first()

    def idt(self):
        user = User.query.filter_by(email=self.eml).first()
        return user.id

class QS():
    def __init__(self, shop_name):
        self.shop_name = shop_name

    def shp(self):
        return Shop.query.filter_by(shop_name=self.shop_name).first()