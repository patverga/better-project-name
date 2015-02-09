from datetime import date
import facebook
import requests
import mongo_wrapper as mongo
import re
__author__ = 'pv'

birthday_regex = re.compile('hap+y+.*b(irth)?day+', re.IGNORECASE)
http_regex = re.compile('https?://\S+\s*')
# def get_user_posts(access_token):
# """
# get all the posts and status updates this user has made
# :param access_token: valid access token for user
# :return: all the posts
#     """
#     graph = facebook.GraphAPI(access_token)
#
#     post_responses = [graph.get_object('me/' + feed_type) for feed_type in ['feed']]  # 'statuses', 'posts']]
#     post_data = [r for d in [response['data'] for response in post_responses if 'data' in response] for r in
#                  d]  # flatten
#     posts = [d['message'] for d in post_data if 'message' in d]
#
#     return posts


## TODO get all pages of comments, make faster
def get_user_posts(access_token, user_name):
    '''    
    :param access_token: User access token
    :return: all the things that come from this person feed
    '''
    last_update = mongo.get_last_user_update(user_name, 'facebook')
    graph = facebook.GraphAPI(access_token)
    # for feed_type in ['statuses', 'posts']:
    posts = graph.get_object('me/feed', since=last_update, until=date.today().isoformat())
    while posts['data']:
        try:
            # all posts
            [mongo.insert_text(user_name, http_regex.sub('', post['message']), 'facebook') for post in posts['data']
             if 'message' in post and 'from' in post and 'name' in post['from'] and user_name == post['from']['name']]
            # all comments
            [mongo.insert_text(user_name, comment['message'], 'facebook') for comment in
             [post['comments'] for post in posts['data'] if 'comments' in post]
             if 'from' in comment and 'name' in comment['from'] and user_name == comment['from']['name']
             and 'message' in comment and birthday_regex.search(comment['message']) is not None]

            posts = requests.get(posts['paging']['next']).json()
        except Exception, e:
            print "Key Error: " + str(e)
    # store current date as last update
    mongo.save_last_user_update(user_name, 'facebook')


def test():
    get_user_posts(
        'CAAFiRqsaAxQBAHDVyZAJ2iLWMxQr1m8Crv3Y9eqE3U8laIIVVMJHEOqcSOacOclg9ks9owYexgZC1O5hlrXmZAZBbNFzZCmjN52QIZCJYw7bcZBgYylkbLarUGyYzRSaveifxex9BhstyHdBN7YodkVS9wLhdpiZBoQCvMZB760ZBoWJeD96jQLxpUPySVDHZBxHNtiMQe0cyPgWNT19dnnPeX5oeWdEfFkcX0ZD'
        , 'Patrick Verga')
    mongo.test()


if __name__ == "__main__":
    test()