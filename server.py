# --- coding: utf-8 ---

# bottleとsqliteを使ってcrud実装
from bottle import route, run, template, request, post, redirect
import sqlite3

'''
ルーティング
'''

# ユーザー一覧ページ
@route('/')
def index():
    user_list = get_users()
    return template('index', user_list=user_list)

@route('/showUser/:id', method=["POST"])
def showUser(id):
    userInfo = get_user(id)
    return template('showUser', userInfo=userInfo)

# 新規ユーザー作成
@route('/createUser', method=["POST"])
def createUser():
    name = request.POST.getunicode('user_name')
    email = request.POST.getunicode('user_email')
    password = request.POST.getunicode('user_password')

    create_user(name,email,password)
    return redirect('/')

# ユーザーの削除
@route('/deleteUser/:id', method=["POST"])
def deleteUser(id):
    delete_user(id)

    return redirect('/')

# ユーザー名の変更
@route('/updateUser/:id', method=["POST"])
def updateUser(id):
    name = request.POST.getunicode("user_name")

    update_user(name, id)
    return redirect("/")

'''
関数
'''

def get_users():
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users"
    c.execute(select)

    return c.fetchall()

def get_user(id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users where id = '{0}'".format(id)
    c.execute(select)

    return c.fetchone()

def create_user(name,email,password):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users order by id desc"
    c.execute(select)

    largest_id = c.fetchone()

    insert = "insert into users(id,name,email,password) values(?,?,?,?)"
    user = (largest_id[0]+1, name, email, password)

    c.execute(insert, user)
    conn.commit()

def delete_user(id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    delete = "delete from users where id = '{0}'".format(id)

    c.execute(delete)
    conn.commit()

def update_user(name, id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    update = "update users set name = ? where id = ?"
    user = (name, id)

    c.execute(update, user)
    conn.commit()


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)