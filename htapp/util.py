import uuid
from datetime import datetime, timedelta
from math import ceil

from sqlalchemy import  create_engine
engine = create_engine('mysqle+pymysql://zsz:123?@127.0.0.1:3306/woaxf')

import hashlib
def enc_pwd(pwd):
    sha256 = hashlib.sha256()
    sha256.update(pwd.encode("utf-8"))
    return sha256.hexdigest()

def create_unique_str():
    uuid_str = str(uuid.uuid4().encode('utf-8'))
    md5= hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()
def data_to_dict(cursor):
    heads = [i[0]for i in cursor.description]
    return [dict(zip(heads,col)) for col in cursor.fetchall]
def get_no_sale():
    con = engine.connect
    five_ten_days = datetime.now()-timedelta(days=15)
    sql = """
        SELECT
           DISTINCT i.goods_id
        FROM 
         axf_order AS o 
        LEFT JOIN
          axf_orderitem AS i
        ON 
           o.id = i.order_id
        WHERE 
            o.create_time > "{my_time}"
        AND 
            o.create_time < now()
          
    """ .format(my_time= five_ten_days)
    res = con.execute(sql)
    goods_ids = data_to_dict(res.cursor)
    goods_tmp = []
    for i in goods_ids:
        goods_tmp.append(list(i.values())[0])
    all_goods_sql = '''
        select id from axf_goods;
    '''
    all_goods = data_to_dict(con.execute(all_goods_sql).cursor)
    all_goods_tmp = []
    for i in all_goods:
        all_goods_tmp.append(list(i.values())[0])
    result = list(set(all_goods_tmp) - set(goods_tmp))
def get_data():
    get_goods_day = 3
    my_time = datetime.now() - timedelta(days=get_goods_day*2)
    sql = '''
       SELECT
         i.goods_id , sum(i.num) AS sum_num
       FROM
         axf_order as o 
       LEFT JOIN
          axf_orderitem AS i
       ON 
          o.id = i.order_id
       WHERE 
           o.create_time > "{my_time}"
        AND 
           o.create_time<now()
        GROUP BY
           i.goods_id
    '''.format(my_time = my_time)
    con = engine.connect()
    res=con.execute(sql)
    result = data_to_dict(res.cursor)
    for i in result:
        i['need'] = ceil((float(i.get('sum_num'))/(get_goods_day * 5) )* get_goods_day)




















