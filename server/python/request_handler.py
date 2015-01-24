from urlparse import parse_qs
from cgi import escape
import mongo_wrapper as mongo
import facebook


def application(environ, start_response):
    status = '200 OK'

    # parse the http request
    request_dict = parse_qs(environ['QUERY_STRING'])
    user_name = escape(request_dict.get('name', [''])[0])
    access_token = escape(request_dict.get('access_token', [''])[0])


    posts = get_user_posts(access_token)
    mongo.insert_access_token(user_name, access_token, 'facebook')

    response = 'Success ' + user_name

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(response)))]
    start_response(status, response_headers)

    return [response]


def get_user_posts(access_token):
    """
    get all the posts and status updates this user has made
    :param access_token: valid access token for user
    :return: all the posts
    """
    graph = facebook.GraphAPI(access_token)

    post_responses = [graph.get_object('me/' + feed_type) for feed_type in ['statuses', 'posts']]
    post_data = [r for d in [response['data'] for response in post_responses if 'data' in response] for r in d]  # flatten
    posts = [d['message'] for d in post_data if 'message' in d]

    return posts