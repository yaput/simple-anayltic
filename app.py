from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
import json
from db_connection import get_all_user_detail, get_fallback_intent
from datetime import datetime

app = Flask(__name__)
CORS(app)  # very important!

##############################################


@app.route('/default-fallback', methods=['POST'])
def unhandled_intent():
    bot_name = request.json['bot_name']
    check_bot = get_fallback_intent(bot_name)
    return jsonify(check_bot)


if __name__ == '__main__':
    app.run(debug=True)
