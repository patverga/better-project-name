__author__ = 'pv'

import pymongo

mongo_ip = 'localhost'
mongo_port = 27017
db_name = "better_database_name"
# db_name = "data_base_name"


def connect(table_name):
    connection = pymongo.Connection(mongo_ip, mongo_port)
    db = connection[db_name]
    return db[table_name]


def insert_access_token(user_name, access_token, source):
    access_tokens = connect(source + "_access_tokens")
    # access_tokens.insert(dict(user_name=user_name, access_token=access_token))#, _id=user_name))

    # we only want 1 token per user, update with a new token if we have it otherwise insert
    access_tokens.update({'user_name': user_name}, {"$set": {"access_token": access_token}}, upsert=True, multi=True)


def get_access_token(user_name, source):
    access_tokens = connect(source + "_access_tokens")
    results = access_tokens.find({'user_name': user_name}, {'access_token': 1, '_id': 0})
    return results[0]['access_token']


def insert_text(user_name, text, source):
    access_tokens = connect(source + "_text")
    access_tokens.insert(dict(user_name=user_name, text=text))


def get_user_text(user_name, source):
    access_tokens = connect(source + "_text")
    results = access_tokens.find({'user_name': user_name}, {'text': 1, '_id': 0})
    return results


def test():
    # table = connect('facebook_text')
    table = connect('facebook_access_tokens')
    # insert_text('test_user', 'a bunch of words text', 'facebook')
    # insert_access_token('Patrick Verga', 'test', 'facebook')
    for r in table.find():
        print r

        # token = get_access_token('Patrick Verga', 'facebook')
        # print token


test()


