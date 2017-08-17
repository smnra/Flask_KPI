# coding=utf-8

from flask import Flask
from flask import render_template,url_for,request,redirect
from wtforms import Form,TextField,PasswordField,validators
import wtforms
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
    return render_template('login.html',message = '请登录!')


class LoginForm(Form):
    username = TextField('username',[validators.Required()])
    password = PasswordField('password',[validators.Required()])
@app.route('/login_wtf',methods = ['GET','POST'])
def login_wtf():
    myform = LoginForm(request.form)
    if request.method =='POST':
        if myform.username.data == 'SMnRa' and myform.password.data == '123456' and myform.validate():
            return render_template('user_wtf.html',form = myform)
        else:
            return render_template('login_wtf.html',message = '用户名或密码错误!',form = myform)
    return render_template('login_wtf.html',form = myform)




if __name__ == '__main__':
    app.run(debug=True,port=80)