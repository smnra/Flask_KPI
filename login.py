# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request

app = Flask(__name__)

@app.route('/login',methods = ['POST','GET'])
def login():
    username = request.form['username']
    password = request.form['password']

    print(username)
    print(password)
    if not username:
        return render_template('login.html',username = '请输入用户名!')
    elif not password:
        return render_template('login.html',password = '请输入用户名!')
    elif username is 'SMnRa' and password is '123456':
        return render_template('main.html',username = username)
    else:
        return render_template('login.html',message = '用户名或密码错误!')





if __name__ == '__main__':
    app.run('127.0.0.1',port = 80)