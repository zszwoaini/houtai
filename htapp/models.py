import datetime

from .ext import db
from .util import enc_pwd

class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    name = db.Column(
        db.String(30),
        nullable=True
    )
    email = db.Column(
        db.String(30),
        unique=True,
        index=True
    )
    pwd = db.Column(
        db.String(255),
        nullable=False
    )
    is_active = db.Column(
        db.Boolean,
        default=False
    )
    is_delete = db.Column(
        db.Boolean,
        default=False
    )
    # orders = db.relationship(
    #     'Order',
    #     backref = 'user',
    #     lazy = True
    # )

    @classmethod
    def creat_user(cls,email, pwd,name=None):
#         email 能不能搜到一个用户 检查email
        users = User.query.filter(User.email==email)
        if users.count() > 0:
            return None
            # raise Exception("该Email以被使用")
#         加密密码
        user_pwd = enc_pwd(pwd)
#     创建用户
        name = name if name else email
        user = cls(
            name=name,
            email=email,
            pwd=user_pwd
        )
        db.session.add(user)
        db.session.commit()
        return user

    # 设置密码
    def set_pwd(self, pwd):
        if not pwd or len(pwd) == 0:
            raise Exception("密码不能为空")
        # 先对密码进行加密 再赋值
        self.pwd = enc_pwd(pwd)
        # 保存到数据库
        db.session.add(self)
        db.session.commit()
        return True
    def check_pwd(self,pwd):
        u_pwd = enc_pwd(pwd)
        if u_pwd == self.pwd:
            return  True
        else:

            return False

class Goods(db.Model):
    __tablename__ = "axf_goods"
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    productid = db.Column(
        db.String(20)
    )
    productimg = db.Column(
        db.String(255)
    )
    productname = db.Column(
        db.String(130),
        nullable=True
    )
    productlongname = db.Column(
        db.String(190)
    )
    isxf = db.Column(
        db.Boolean,
        default=False
    )
    pmdesc = db.Column(
        db.Boolean,
        default=False
    )
    specifics = db.Column(
        db.String(40)
    )
    price = db.Column(
        db.Float
    )
    marketprice = db.Column(
        db.Float
    )
    categoryid = db.Column(
        db.Integer
    )
    childcid = db.Column(
        db.Integer
    )
    childcidname = db.Column(
        db.String(30)
    )
    dealerid = db.Column(
        db.String(30)
    )
    storenums = db.Column(
        db.Integer
    )
    productnum = db.Column(
        db.Integer
    )
    order_item_goods = db.relationship(
        'OrderItem',
        backref = 'goods',
        lazy = True
    )
class Order(db.Model):
    __tablename__ = 'axf_order'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True

    )
    user_id = db.Column(
        db.Integer,
        # db.ForeignKey('axf_myuser.id')
    )
    create_time = db.Column(
        db.DateTime,
        default=datetime.datetime.now
    )
    status = db.Column(
        db.Integer
    )
    order_items = db.relationship(
        'OrderItem',
        backref = 'order',
        lazy = True
    )
class OrderItem(db.Model):
    __tablename__ = 'axf_orderitem'
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    order_id = db.Column(
        db.Integer,
        db.ForeignKey('axf_order.id')
    )
    goods_id = db.Column(
        db.Integer,
        db.ForeignKey('axf_goods.id')

    )
    num = db.Column(
        db.Integer
    )
    buy_money = db.Column(
        db.Numeric(precision=10,scale=2)
    )


