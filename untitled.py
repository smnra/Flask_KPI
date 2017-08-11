from flask import Flask
import pandas as pd
from sqlalchemy import create_engine

word = ""

sql = "select * from wcdma_day where 地市 <>'其他'  AND   日期>= '20170731' AND 日期 <  '20170901'"
engine = create_engine('mysql+pymysql://root:10300@192.168.3.74:50014/3g_kpi_browsing?charset=utf8')
#df.to_sql('tick_data',engine,if_exists='append')#存入数据库，这句有时候运行一次报错，运行第二次就不报错了，不知道为什么
df1 = pd.read_sql(sql,engine)    #read_sql直接返回一个DataFrame对象      设置多个index，只要将index_col的值设置为列表

app = Flask(__name__)


@app.route('/index.html')
def index():
    return str(df1)

if __name__ == '__main__':
    app.run(debug= True)
