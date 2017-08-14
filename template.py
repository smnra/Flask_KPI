#coding=utf-8
import flask
from flask import Flask,render_template,request
import user_class

app = Flask(__name__)
@app.route('/<content>')
def index(content):
    #content = content
    return render_template('template_1.html',content = content)   #第一个content 模版template_1.html中的{{content}},第二个content为函数index(content)中的content 即'/<content>' 中的content

@app.route('/user')
def user():
    user = user_class.User('SMnRa',12)
    inputid = request.args.get('id')
    print(type(inputid))
    print(type(user.id))
    if int(inputid) == 12:
        return render_template('user_index.html',username = user.name,userid = user.id)
    else:
        return render_template('template_1.html',content = "Not Found user id, and id is %s" % inputid)


@app.route('/users')
def users():
    userss = []
    for i in range(1,10):
        userss.append(user_class.User('smnra_'+str(i),i))
    return render_template('for_index.html',userss=userss)



@app.route('/select_user')
def sel_user():
    user = None
    inputid = int(request.args.get('id'))
    if inputid == 12:
        user = user_class.User('SMnRa',12)
    return render_template('user_index_1.html',user = user)


if __name__ == '__main__':
    app.run()