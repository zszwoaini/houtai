from flask import request, render_template
from flask_mail import Message
from flask_restful import Resource, reqparse, fields, marshal_with

from htapp.models import *
from htapp.util import create_unique_str
from htapp.task import send_email
from htapp.ext import mail, cache

public_fields = {
    "code": fields.Integer(default=1),
    "msg": fields.String(default="ok"),
    "data": fields.String()
}

register_parse = reqparse.RequestParser()
register_parse.add_argument("email", required=True, location="form", help="email必填")
register_parse.add_argument("pwd", required=True, location="form", help="密码必填")
register_parse.add_argument("confirm_pwd", required=True, location="form", help="确认密码必填")

class RegisterAPI(Resource):

    @marshal_with(public_fields)
    def post(self):
        params = register_parse.parse_args()

        email = params.get("email")
        pwd = params.get("pwd")
        confirm_pwd = params.get("confirm_pwd")

        # 判断密码和确认密码是否一致
        if pwd != confirm_pwd:
            return {"code": 2, "msg": "密码和确认密码不一致"}

        res = User.creat_user(email=email, pwd=pwd)
        # 给你发个邮件 让你激活
        url = "http://" + request.host + "/active/" + create_unique_str()
        print(url)

        if res:
            # send_email.delay(email, url, res.id, mail)

            msg = Message("欢迎注册爱鲜蜂后台管理",
                          [email],
                          sender="1181233464@qq.com"
                          )
            msg.html = render_template("active.html", url=url)
            mail.send(msg)

            key = url.split("/")[-1]
            cache.set(key, res.id, timeout=60*60)
            return {"data": "/index"}
        else:
            return {"code": 3, "msg": "注册失败"}
item_parse = reqparse.RequestParser()
item_parse.add_argument('g_id',type=int,required=True,location='form',help='g_id必填参数')
patch_parse = item_parse.copy()
patch_parse.add_argument('price',type=float,location='form')
patch_parse.add_argument('specifices',location='form')
class ItemAPI(Resource):
    @marshal_with(public_fields)
    def delete(self):
        g_id = item_parse.parse_args().get('g_id')
        goods = Goods.query.get_or_404(g_id)
        db.session.delete(goods)
        db.session.commit()
        return {'data':'deleted'}
    def patch(self):
        par = patch_parse.parse_args()
        g_id = par.get('g_id')
        goods = Goods.query.get(g_id)
        price = par.get('price',goods.pirce)
        unit = par.get("specifics", goods.specifics)
        #修改
        goods.price=price
        goods.specifics=unit
        db.session.delete(goods)
        db.session.commit()
        return {'data': 'updata'}









