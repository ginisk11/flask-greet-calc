from flask import Flask
app=Flask(__name__)
@app.route("/welcome")
def hello_world1():
   return "welcome"
@app.route("/welcome/home")
def hello_world2():
    return "welcome home"
@app.route("/welcome/back")
def hello_world3():
    return "welcome back"