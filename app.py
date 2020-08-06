#Flaskからimportしてflaskを使えるようにする
from flask import Flask,render_template
 
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













if __name__ == "__main__":
    #flaskが持っている開発者用サーバを実行します
    app.run(debug=True)

