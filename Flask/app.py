
from flask import Flask, request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/hello2")
def hello_world2():
    return "<h1>Hello World 2</h1>"

@app.route("/hello3")
def hello_world3():
    return "<h1>Hello World 3</h1>"

@app.route("/result")
def test():
    a=5+6
    return "<h2>This is the Answer of a : {}</h2>".format(a)

@app.route("/req")
def req():
    data=request.args.get('x')
    return "This is my input from url {}".format(data)

if __name__=="__main__":
    app.run(host="0.0.0.0")