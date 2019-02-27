from flask import Blueprint, render_template, request, jsonify
from .models import *
blue = Blueprint("axfbg", __name__)

def init_blue(app):
    app.register_blueprint(blue)


# 写一些视图函数
@blue.route("/")
def item_view():


    page = request.args.get('page',1)
    pagination = Goods.query.paginate(int(page),10)




    return render_template("item/item.html",pagination=pagination,goods= pagination.items)
@blue.route('/item_serch')
def item_serch():

    kw = request.args.get('kw')
    pagination = Goods.query.filter(Goods.productlongname.like("%"+kw+"%")).paginate(1,10)
    return render_template('item/item.html',pagination=pagination,kw=kw,goods = pagination.items)


@blue.route("/order_manage")
def order_manage():
    stutas_map = {
        1:"待付款",
        2:"已付款",
        3:"已发货",
        4: "已收货",
        5:"待评价",
        6:"已评价"
    }


    page = request.args.get('page', 1)
    pagination = Order.query.paginate(int(page), 2)


    for i in pagination.items:
        i.created_time = i.create_time.strftime('%y年%m月%d日 %H:%M:%S')
        i.sum_money = 0
        for j in i.order_items:
            sum_money = i.sum_money +j.num*j.buy_money
        i.sum_money = sum_money
        i.ch_status = stutas_map.get(i.status)






    return render_template("order/order_index.html",pagination=pagination, data=pagination.items)

@blue.route("/nosale")
def nosale():

    return render_template("nosale/nosale.html")


@blue.route("/auto_bh")
def auto_bh():
    return render_template("auto/auto.html")

@blue.route("/indf",methods=['GET','POST'])
def index():
    if request.method == 'GET':
      return render_template("index/index.html")
    if request.method == 'POST':
        par =request.form
        email = par.get('email')
        pwd = par.get('pwd')
        if not all([email, pwd]):
            data = {

                "code": 2,
                "msg": "账号或密码不能为空",
                "data": ""
            }

        return jsonify (data)
    # users = User.query.filter(User.email == email)
    # if users:
    #     if







@blue.route("/register")
def register_view():
    return render_template("register/register.html")