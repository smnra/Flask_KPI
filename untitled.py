# coding=utf-8
from flask import Flask
from flask import request,url_for
import pandas as pd
from sqlalchemy import create_engine
import flask
word = ""

sql = "select * from wcdma_day where 地市 <>'其他'  AND   日期>= '20170731' AND 日期 <  '20170801'"
engine = create_engine('mysql+pymysql://root:10300@192.168.3.74:50014/3g_kpi_browsing?charset=utf8')
#df.to_sql('tick_data',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
df1 = pd.read_sql(sql,engine)    #read_sql直接返回一个DataFrame对象      设置多个index，只要将index_col的值设置为列表

app = Flask(__name__)


@app.route('/')
def index():
    return str(df1)

@app.route('/user/<id>')            #获取url中的一部分
def user(id):
    return '<H1>Hello,%s!</H1>' % id

@app.route('/query_user')           #url 键值对 获取
def query_user():
    id = request.args.get('id')
    type = request.args.get('type')
    return '<H2>query_user:%s!</H2> <h1>type is %s</h1>' %(id ,type)

@app.route('/query_url/<fun>')            #反响路由查询  根据url中给出的fun 函数名 查询 相应的url
def query_url(fun):
    url = url_for(fun)
    return '<h2>The Function: %s </h2> <h2> The URL is: %s</h2>' %(fun,url)



if __name__ == '__main__':
    app.run()
