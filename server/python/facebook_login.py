from urlparse import parse_qs
from cgi import escape
import mongo_wrapper as mongo
import facebook_utils as fb_util
import generate_text_markov as mc


def application(environ, start_response):
    status = '200 OK'

    # parse the http request
    request_dict = parse_qs(environ['QUERY_STRING'])
    user_name = escape(request_dict.get('name', [''])[0])
    access_token = escape(request_dict.get('access_token', [''])[0])
    
    # save access token
    mongo.insert_access_token(user_name, access_token, 'facebook')
    # get and save all the posts
    fb_util.get_user_posts(access_token, user_name)

    # make and return response
    response = 'Success ' + user_name + "\n"
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(response)))]
    start_response(status, response_headers)

    return [response]
