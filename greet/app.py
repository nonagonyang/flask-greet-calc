from flask import Flask
app=Flask(__name__)
@app.route("/welcome")
def welcome():
    return "Welcome"
@app.route("/welcome/<subpage>")
def welcome(subpage):
    return f"Welcome {subpage}"
