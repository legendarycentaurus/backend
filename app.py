from flask import Flask,send_from_directory,render_template
import time,json,os
from datetime import datetime
from pip._vendor import requests
from flask_cors import CORS,cross_origin

#app = Flask(__name__, static_url_path='', static_folder="../frontend/build")
app = Flask(__name__);
CORS(app)
#os.environ['SECRET_KEY']="nand"
app.config["SECRET_KEY"]= os.environ['SECRET_KEY']


@app.route("/")
def hello_world():
    #response = requests.get("https://api.mfapi.in/mf")
    #print(response.json())
    #data = response.json()
    #out_file = open("myfile.json", "w")
    #json.dump(data[-5:], out_file, indent = 6)
    #out_file.close()

    return "<p>Hello, Index page !</p>"+app.config["SECRET_KEY"];#send_from_directory(app.static_folder,'index.html');#render_template("index.html");

@app.route("/user/<userName>")
def printUserName(userName):
    return "<p>Hello, "+userName+"!</p>" 

@app.route('/time', methods=['GET'])
@cross_origin()
def get_current_time():
    print("Someone called /time API");
    return {'time': time.time()}

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Sorry!! Page not Found!!!!</p>",404       


@app.errorhandler(500)
def internal_eror(e):
    return "<p>Sorry!! Server Error!!!!</p>" ,500          