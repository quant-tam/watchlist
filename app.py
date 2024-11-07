from flask import Flask, render_template
from markupsafe import escape

# 创建一个程序对象app
app = Flask(__name__)

name = "Sting Tam"
movies = [
    {"title": "My Neighbor Totoro", "year": "1988"},
    {"title": "Dead Poets Society", "year": "1989"},
    {"title": "A Perfect World", "year": "1993"},
    {"title": "Leon", "year": "1994"},
    {"title": "Mahjong", "year": "1996"},
    {"title": "Swallowtail Butterfly", "year": "1996"},
    {"title": "King of Comedy", "year": "1999"},
    {"title": "Devils on the Doorstep", "year": "1999"},
    {"title": "WALL-E", "year": "2008"},
    {"title": "The Pork of Music", "year": "2012"},
]

# 注册一个处理函数，官方叫视图函数(view function)
# 装饰器app.route()绑定对应的URL
# 用户访问这个URL时，就会触发这个函数，获取返回值，并显示在浏览器窗口
# 一个试图函数可以绑定多个URL，这通过附加多个装饰器实现
# @app.route('/index')
# @app.route('/home')
@app.route("/")
def index():
    return render_template("index.html", name=name, movies=movies)
    # return "欢迎来到我的 Watchlist!"
    # return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


# 在 URL 里定义变量部分<name>
# @app.route("/user/<name>")
# def user_page(name):
# escape() 函数对 name 变量进行转义处理，比如把 < 转换成 &lt;。
# 防止把他们当作代码执行，以免包含恶意代码
# return f"User: {escape(name)}"


# url_for 函数来生成 URL，它接受的第一个参数就是端点值
# @app.route("/test")
# def test_url_for():
# 下面是一些调用示例（请访问 http://localhost:5000/test 后在命令行窗口查看输出的 URL）：
# print(url_for("hello"))
# print(url_for("user_page", name="sting"))
# print(url_for("user_page", name="daemon"))  # /user/daemon
# print(url_for("test_url_for"))  # /test
# print(url_for("test_url_for", num=2))  # /test?num=2
# return "Test Page"
