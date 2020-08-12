#Flaskからimportしてflaskを使えるようにする
from flask import Flask,render_template,request,session,redirect
import sqlite3
 
#appっていう名前でFlaskアプリをつくっていくよ～みみたいな
app  = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World."

@app.route("/template/<name>")
def greet(name):
    return name + "さん、ハロー！"

@app.route("/template")
def template():
    py_name  = "ライフライン"
    return  render_template("index.html",name = py_name)

@app.route("/sarada")
def sarada():
    return render_template("sarada.html")



@app.route("/weather")
def weather():
    py_weather  = "晴れ"
    return  render_template("weather.html",weather = py_weather)


@app.route("/dbtest")
def dbtest():
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
    #課題１ スタッフの誰か一名 （誰でも可）情報を取得するSQL
    c.execute('SELECT  name,age,address from staff where id=2')
    staff_info = c.fetchone()
    c.close()
    print(staff_info)

    #課題２ スタッフの誰か一名（誰でも可）情報を表示するHTMLを作成し表示
    return render_template("dbtest.html",staff_info = staff_info)




# todolist

@app.route("/task_list")
def task_list():
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()

    c.execute('SELECT * from task')
    task_list =[]


    for row in c.fetchall():
        task_list.append({"id":row[0], "task":row[1], "limit":row[2]})
    c.close()
    print(task_list)

    return render_template("tasklist.html",task_list=task_list)

# 追加送信機能


@app.route("/add",methods=["GET"])
def add_get():
    return render_template("add.html")



@app.route("/add",methods=["POST"])
def add_post():
    name = request.form.get("task")
    limit = request.form.get("task_limit")
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()
    c.execute('insert into task values(null,?,?)',(name,limit))
    conn.commit()
    conn.close
    print(task_list)

    return redirect("/task_list")

# 編集機能追加
@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("tasklist.db")  #データベースに接続
    c = conn.cursor()
    c.execute('select * from task where id = ?',(id,))
    task_list = c.fetchone() #タスクからとってきてね
    conn.close
    if task_list is not None:
        task = task_list[1]
        limit = task_list[2]
    else:
        return "タスクはありません"

    item = {"id":id,"task":task,"limit":limit}

    return render_template("/edit.html", task = item)

@app.route("/edit",methods=["POST"])
def update_task():
    item_id = request.form.get("task_id")
    task = request.form.get("task")
    limit = request.form.get("limit")
    conn = sqlite3.connect("tasklist.db")
    c = conn.cursor()
    # c.execute('update name limit set task = ?,limit = ? where id = ?,',(task,limit,item_id))
    c.execute('update task set name = ? ,task_limit = ? where id = ?',(task,limit,item_id))
    conn.commit()
    conn.close()

    return redirect("/task_list")

@app.errorhandler(404)
def notfound(code): 
    return "ようこそ！404だよ！！！"

# 削除機能追加
@app.route("/delete/<int:id>")
def delete_task(id):
    conn = sqlite3.connect("tasklist.db")  #データベースに接続
    c = conn.cursor()
    c.execute('delete from task where id = ?',(id,))
    conn.commit() 
    conn.close
    return redirect("/task_list")




if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)

