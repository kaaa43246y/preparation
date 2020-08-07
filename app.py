#Flaskからimportしてflaskを使えるようにする
from flask import Flask,render_template,sqlite3
 
#appっていう名前でFlaskアプリをつくっていくよ～みみたいな
app  = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello World."

@app.route("/<name>")
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
    c.excute("SELECT * FROM staff where "カンパネルラ")
    staff_info = c.fetchone()
    c.close()
    print(staff_info)

    #課題２ スタッフの誰か一名（誰でも可）情報を表示するHTMLを作成し表示
    return render_template("")



if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)

