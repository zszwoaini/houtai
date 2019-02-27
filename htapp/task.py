from celery import Celery
from flask import render_template
from flask_mail import Message



app = Celery(__name__)
app.config_from_object('celery_conf')
@app.task
def send_email(reciver,url,u_id,cache,mail):
    msg = Message("欢迎注册爱鲜蜂后台",
                  [reciver],
                  sender='1181233464@qq.com'
                  )
    msg.html = render_template('active.html',url=url)
    mail.send(msg)
    key = url.split('/')[-1]

    cache.set(key,u_id, timeout=60*60)
