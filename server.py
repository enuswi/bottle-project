# --- coding: utf-8 ---

# bottleとsqliteを使ってcrud実装
from bottle import route, run, template, request, post, redirect, static_file
import sqlite3

###################################
# ルーティング
###################################


# ユーザー一覧ページ
@route('/')
def index():
    user_list = get_users()
    return template('index', user_list=user_list)


# ユーザー詳細ページ
@route('/showUser/:user_id', method=["POST"])
def post_show_user(user_id):
    user_info = get_user(user_id)
    return template('showUser', user_info=user_info)


# 新規ユーザー作成
@route('/createUser', method=["POST"])
def post_create_user():
    name = request.POST.getunicode('user_name')
    email = request.POST.getunicode('user_email')
    password = request.POST.getunicode('user_password')

    create_user(name, email, password)
    return redirect('/')


# ユーザーの削除
@route('/deleteUser/:id', method=["POST"])
def post_delete_user(user_id):
    delete_user(user_id)

    return redirect('/')


# ユーザー名の変更
@route('/updateUser/:id', method=["POST"])
def post_update_user(user_id):
    name = request.POST.getunicode("user_name")

    update_user(name, user_id)
    return redirect("/")


# 静的ファイル
@route('/static/<file_path:path>')
def css_static(file_path):
    return static_file(file_path, root="./static")

###################################
# 関数
###################################

def get_users():
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users"
    c.execute(select)

    return c.fetchall()


def get_user(user_id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users where id = '{0}'".format(user_id)
    c.execute(select)

    return c.fetchone()


def create_user(name, email, password):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    select = "select * from users order by id desc"
    c.execute(select)

    largest_id = c.fetchone()

    insert = "insert into users(id,name,email,password) values(?,?,?,?)"
    user = (largest_id[0] + 1, name, email, password)

    c.execute(insert, user)
    conn.commit()


def delete_user(user_id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    delete = "delete from users where id = '{0}'".format(user_id)

    c.execute(delete)
    conn.commit()


def update_user(name, user_id):
    conn = sqlite3.connect('./databases/bottle_project.db')
    c = conn.cursor()

    update = "update users set name = ? where id = ?"
    user = (name, user_id)

    c.execute(update, user)
    conn.commit()


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
