from flask import Blueprint,jsonify
from flask_cors import CORS,cross_origin
from pip._vendor import requests
from bs4 import BeautifulSoup

newroutes = Blueprint('newroutes', __name__)

@newroutes.route('/timedifference/<fromCity>/<toCity>')
@cross_origin()
def newroute(fromCity,toCity):
    try:
        URL='https://24timezones.com/difference/'+fromCity+'/'+toCity;
        page = requests.get(URL);
        soup = BeautifulSoup(page.content, 'html5lib');
        timedifference=soup.select_one("ul ~ p");
        clockFromTime=soup.find('div',{"class":"compare-time"}).findAll('p')
        clockFromTime=clockFromTime[:-1]
        message=[];
        message.append(timedifference.getText( strip=True))
        for row in clockFromTime:
            print(row.text);
            message.append(row.text)
    except:
         message.append("Error kindly contact Nantha Kumar")
    return jsonify({'message': message})