import json

import pymongo
from bson import json_util
from bson.code import Code
connection = pymongo.MongoClient('mongodb://BluebotLog:bluelogic123@18.222.189.3:27017/chatlog')
db = connection['chatlog']


def get_all_user_detail(collection):
    try:
        return json.loads(json_util.dumps(db.get_collection(collection).find()))
    except ValueError as e:
        return e


def get_fallback_intent(collection):
    reduce = Code(open("query_js/reduce.js").read())
    mapping = Code(open("query_js/fallback_map.js", "r").read())
    try:
        result = json.loads(json_util.dumps(db.get_collection(collection).map_reduce(mapping, reduce, out={'inline': 1},
                                                                                     full_response=False)))
        return result
    except ValueError as e:
        return e


def all_intent_selected(collection):
    reduce = Code(open("query_js/reduce.js").read())
    mapping = Code(open("query_js/all_intent_map.js", "r").read())
    try:
        result = json.loads(json_util.dumps(db.get_collection(collection).map_reduce(mapping, reduce, out={'inline': 1},
                                                                                     full_response=False)))
        return result
    except ValueError as e:
        return e

