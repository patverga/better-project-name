import facebook

__author__ = 'pv'


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