# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request

app = Flask(__name__)

@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'SMnRa' and password == '123456':
            return render_template('user.html',username = username)
        else:
            return render_template('login.html',message = '用户名或密码错误!')
    return render_template('login.html',message = '用户名或密码错误!')




if __name__ == '__main__':
    app.run()