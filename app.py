from flask import Flask,send_from_directory,render_template,url_for
from mutual_funds import mutualfunds
from myroutes.new_routes import newroutes
from flask import jsonify;
import time,json,os
from datetime import datetime
from pip._vendor import requests
from flask_cors import CORS,cross_origin
from mftool import Mftool
from bs4 import BeautifulSoup

#app = Flask(__name__, static_url_path='', static_folder="../frontend/build")
app = Flask(__name__);
app.register_blueprint(mutualfunds);
app.register_blueprint(newroutes);
CORS(app)
#os.environ['SECRET_KEY']="nand"
app.config["SECRET_KEY"]= os.environ['SECRET_KEY']


@app.route("/")
@cross_origin()
def hello_world():
    curr_time = time.localtime();
    print(curr_time);
    return "<p>Hello, Index page !</p>"+app.config["SECRET_KEY"];#send_from_directory(app.static_folder,'index.html');#render_template("index.html");


@app.route("/user/<userName>")
@cross_origin()
def printUserName(userName):
    return "<p>Hello, "+userName+"!</p>" 

@app.route("/api/v1/getAllMutualFunds", methods=['GET'])
@cross_origin()
def getAllMutualFunds():
    data = requests.get("https://api.mfapi.in/mf");
    data = data.json();
    data= sorted(data,key=lambda record: record['schemeName'])[0:101];
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response;

@app.route("/api/v1/getMFapi", methods=['GET'])
@cross_origin()
def getMFapi():
    mf = Mftool()
    print(mf);
    mf.get_all_amc_profiles(True)
    data =mf.get_scheme_codes(as_json=True);
    #data = data.items();
    response = app.response_class(
        response=data,
        status=200,
        mimetype='application/json'
    )

    return response;    


@app.route('/time', methods=['GET'])
@cross_origin()
def get_current_time():
    print("Someone called /time API");
    return {'time': time.time()}

@app.route("/getAMC")
@cross_origin()
def printAMC():
    URL="https://groww.in/mutual-funds/amc";
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())
    table = soup.findAll('div', attrs = {'class':'amcBoxDiv213'})
    images=soup.findAll('img')
    print(images);
    amcNames=[];
    for row in table:
        amc = {}
        amc['img']=row.div.div.img['src'];
        amc['name'] = row.b.text; 
        amcNames.append(amc)
    print(amcNames)
    return "<p>Hello, AMC List!</p>" 


@app.errorhandler(404)
def page_not_found(e):
    return "<p>Sorry!! Page not Found!!!!</p>",404       


@app.errorhandler(500)
def internal_eror(e):
    return "<p>Sorry!! Server Error!!!!</p>" ,500          