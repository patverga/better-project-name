from datetime import date

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
    # we only want 1 token per user, update with a new token if we have it otherwise insert
    access_tokens.update({'user_name': user_name}, {"$set": {"access_token": access_token}}, upsert=True, multi=True)


def get_access_token(user_name, source):
    access_tokens = connect(source + "_access_tokens")
    results = access_tokens.find({'user_name': user_name}, {'access_token': 1, '_id': 0})
    return results[0]['access_token']


def insert_text(user_name, text, source):
    if text.strip():
        text_table = connect(source + "_text")
        # text_table.ensure_index({'user_name': 1, 'text': 1}, {'unique': True})
        text_table.insert(dict(user_name=user_name, text=text))


def get_user_text(user_name, source):
    text_table = connect(source + "_text")
    results = [t['text'] for t in text_table.find({'user_name': user_name}, {'text': 1, '_id': 0})]
    return results


def save_last_user_update(user_name, source):
    cur_date = date.today().isoformat()
    update_table = connect(source + "_last_update")
    update_table.update({'user_name': user_name}, {"$set": {"last_update": cur_date}}, upsert=True, multi=True)


def get_last_user_update(user_name, source):
    update_table = connect(source + "_last_update")
    last_update = [d['last_update'] for d in update_table.find({'user_name': user_name}, {'last_update': 1, '_id': 0})]
    return last_update[0] if len(last_update) > 0 else '1979-06-09'


def test():
    table = connect('facebook_text')
    # table = connect('facebook_last_update')
    # insert_text('test_user', 'a bunch of words text', 'facebook')
    # insert_access_token('Patrick Verga', 'test', 'facebook')
    for r in table.find():
        print r
    print '\n'.join(get_user_text('Emma Strubell', 'facebook'))
        # token = get_access_token('Patrick Verga', 'facebook')
        # print token

if __name__ == "__main__":
    test()
