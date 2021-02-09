import spacy
from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
#from addressnet.predict import predict_one
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/extractaddress", methods=["GET","POST"])
@cross_origin()
def extractaddress():
    #return(predict_one("casa del gelato, 10A 24-26 high street road mount waverley vic 3183"))
    return("Hello")