from flask import Blueprint
from flask_cors import CORS,cross_origin

mutualfunds = Blueprint('mutualfunds', __name__)

@mutualfunds.route('/mutualfundtext')
@cross_origin()
def mutualfundtext():
    return "This is a mutual fund"