__author__ = 'pv'

import pymongo

mongo_ip = 'localhost'
mongo_port = 27017
db_name = "data_base_name"


def connect():
    connection = pymongo.Connection(mongo_ip, mongo_port)
    return connection[db_name]


def insert_access_token(user, access_token, source):
    db = connect()
    access_tokens = db[source+"_access_tokens"]
    access_tokens.insert(dict(user_name=user, access_token=access_token))


def test():
    db = connect()
    table = db["facebook_access_tokens"]
    for r in table.find():
        print r


test()