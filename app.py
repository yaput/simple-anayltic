from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
import json
app = Flask(__name__)
CORS(app) # very important!

############################################
"""
connection mongodb
"""
connection = MongoClient('mongodb://BluebotLog:bluelogic123@18.222.189.3:27017/chatlog')
db = connection['chatlog']
"""
until here
"""
##############################################


# @app.route('/avivo', methods=['GET'])
# def get_all_avivo():
#   avivo = db.avivo.find()
#   return jsonify(json.dumps(avivo))


if __name__ == '__main__':
    app.run(debug=True)
