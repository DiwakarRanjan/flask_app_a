from flask import Flask
from flask import request

app= Flask(__name__)

@app.route("/")
def hello_world3():
    return"<h1>Hello,World 3 !</h1>"

@app.route("/Hello,World 1")
def hello_world1():
    return"<h1>Hello,World 1</h1>"

@app.route("/Hello,World 2")
def hello_world2():
    return"<h1>Hello,World 2</h1>"

@app.route("/test")
def test():
    a=5+6+6+8+2
    return "this is my find  name{}".format(a)

@app.route("/test2")
def test2():
    data=request.args.get('x')
    return '''this is a data input from my url {}'''.format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")