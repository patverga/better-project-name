from cgi import escape
from urlparse import parse_qs

__author__ = 'pv'


import sys
from pprint import pprint
from random import choice
import mongo_wrapper as mongo
import facebook_utils as fb_util

EOS = ['.', '?', '!']


def build_dict(words):
    """
    Build a dictionary from the words.

    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in d:
            d[key] = []
        #
        d[key].append(third)

    return d


def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)

    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key

    return ' '.join(li)


def application(environ, start_response):
    # parse the http request
    request_dict = parse_qs(environ['QUERY_STRING'])
    user_name = escape(request_dict.get('name', [''])[0])
    # access_token = mongo.get_access_token(user_name, 'facebook')
    access_token = mongo.get_access_token(user_name, 'facebook')


# get posts from fb api
    posts = fb_util.get_user_posts(access_token)

    # generate dictionary
    text = '\n'.join(posts)
    dictionary = build_dict(text)
    sentence = generate_sentence(dictionary).encode('utf-8')
    # sentence = ''

    start_response('200 OK', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(sentence)))
    ])

    return [sentence]


####################

def test():
    user_name = "Emma Strubell"
    access_token = mongo.get_access_token(user_name, 'facebook')
    posts = fb_util.get_user_posts(access_token)
    text = '\n'.join(posts)
    print text

    words = text.split()
    dictionary = build_dict(words)
    sentence = generate_sentence(dictionary)
    print(sentence)

if __name__ == "__main__":
    test()
