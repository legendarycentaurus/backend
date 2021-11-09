from flask import Flask,send_from_directory,render_template
import time
from datetime import datetime

app = Flask(__name__, static_url_path='', static_folder="../frontend/build")
app.config["Secret_key"]="nanda kumar"


@app.route("/")
def hello_world():
    return send_from_directory(app.static_folder,'index.html');#render_template("index.html");

@app.route("/user/<userName>")
def printUserName(userName):
    return "<p>Hello, "+userName+"!</p>" 

@app.route('/time')
def get_current_time():
    print("Someone called /time API");
    return {'time': time.time()}

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Sorry!! Page not Found!!!!</p>",404       


@app.errorhandler(500)
def internal_eror(e):
    return "<p>Sorry!! Server Error!!!!</p>" ,500          