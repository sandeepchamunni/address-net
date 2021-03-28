from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from addressnet.predict import predict_one
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/extractaddress", methods=["GET","POST"])
@cross_origin()
def extractaddress():
    return(str(predict_one(request.args.get('fulladdress'))))