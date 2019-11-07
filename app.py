from flask import Flask, jsonify, request
from flask_cors import CORS
from db_connection import get_fallback_intent, all_intent_selected
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = Flask(__name__)
CORS(app)  # very important!

##############################################


@app.route('/intent-default-fallback', methods=['POST'])
def unhandled_intent():
    bot_name = request.json['bot_name']
    check_bot = get_fallback_intent(bot_name)
    for i in check_bot['results']:
        i['text'] = i.pop('_id')
        i['count'] = i.pop('value')
    pd.read_json(check_bot['results'])
    return jsonify(check_bot['results'])


@app.route('/intent-in', methods=['POST'])
def all_intent():
    bot_name = request.json['bot_name']
    check_bot = all_intent_selected(bot_name)
    for i in check_bot['results']:
        i['intent'] = i.pop('_id')
        i['count'] = i.pop('value')
    return jsonify(check_bot['results'])


if __name__ == '__main__':
    app.run(debug=True)
