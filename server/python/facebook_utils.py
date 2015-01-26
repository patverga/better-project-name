import facebook
import requests
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

# def all_user_posts(access_token, user_name):
#     graph = facebook.GraphAPI(access_token)
#     all_posts = []
#     for feed_type in ['statuses', 'posts']:
#         posts = graph.get_object('me/'+feed_type)
#         while posts['data']:
#             try:
#                 for post in posts['data']:
#                     # grab each post/status text
#                     if 'message' in post:
#                         all_posts.append(post['message'])
#                     # get all the comments by this user
#                     if 'comments' in post:
#                         all_posts.append(all_post_comments(post, user_name))
#                 # get all pages of results
#                 posts = requests.get(posts['paging']['next']).json()
#             except KeyError:
#                 print "Key Error"
#     return all_posts
#
#
# def all_post_comments(post, user_name):
#     user_comments = []
#     comments = post['comments']
#     while comments['data']:
#         try:
#             for comment in comments['data']:
#                 # grab if this user wrote it
#                 if 'from' in comment and 'name' in comment['from'] and user_name is comment['from']['name']:
#                     user_comments.append(comment['message'])
#             # get all pages of results
#             comments = requests.get(comments['paging']['next']).json()
#         except KeyError:
#             print "Key Error"
#     return user_comments
#
#
# print all_user_posts('CAAFiRqsaAxQBADpbXrKeL5ub8hADnv43mtSVjiHkhIiU7Vxx8J0ghQzg3q56Kdlg7n2ddZCC5ViJoOUpamhvI5YvGi6tcEYf6QNgMC2GZA54lmIPasRWVb7nZCwKplgRbN6MRXsJAZCZBM7cbKFKmk0qClIOvSpAZBvNos2ZB0WgYQltkOMg1YpT4LS8QNBZCTPoUcPZAQSYsRmMGalkcXHcHIWQwvJUqyzIZD')