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

    return str(' '.join(li)).encode('utf-8')


def application(environ, start_response):
    # parse the http request
    request_dict = parse_qs(environ['QUERY_STRING'])
    user_name = escape(request_dict.get('name', [''])[0])

    # get posts from fb api
    posts = mongo.get_user_text(user_name, 'facebook')

    # generate dictionary
    dictionary = build_dict('\n'.join(posts).split())
    # sentence = u'poop poop lots of poop butts butt butt'.encode('utf-8')
    sentence = generate_sentence(dictionary)#.encode('utf-8')
    # sentence = ''.join([c for c in generate_sentence(dictionary)])

    start_response('200 OK', [
        ('Content-Type', 'text/plain; charset=utf-8'),
        ('Content-Length', str(len(sentence)))
    ])

    return [sentence]


####################

def test():
    user_name = "Emma Strubell"
    access_token = mongo.get_access_token(user_name, 'facebook')
    posts = fb_util.get_user_posts(access_token)
    text = '\n'.join(posts)
    # print text

    words = text.split()
    dictionary = build_dict(words)
    sentence = generate_sentence(dictionary)
    print(sentence)

if __name__ == "__main__":
    test()
