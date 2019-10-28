from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
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


def get_collection_names(bot_name):
    collections = json.loads(json_util.dumps(db.list_collection_names()))
    if bot_name in collections:
        return 200
    else:
        return 500


@app.route('/bot-detail', methods=['POST'])
def bot_data():
    bot_name = request.json['bot_name']
    check_bot = get_collection_names(bot_name)
    if check_bot == 200:
        bot_load = json.loads(json_util.dumps(db.get_collection(bot_name).find()))
        print(bot_load)
        return jsonify(bot_load)
    else:
        return jsonify(message="Please Contact Administrator", status=500)


if __name__ == '__main__':
    app.run(debug=True)
