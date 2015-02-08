import facebook
import requests

__author__ = 'pv'


# def get_user_posts(access_token):
# """
# get all the posts and status updates this user has made
#     :param access_token: valid access token for user
#     :return: all the posts
#     """
#     graph = facebook.GraphAPI(access_token)
#
#     post_responses = [graph.get_object('me/' + feed_type) for feed_type in ['feed']]  # 'statuses', 'posts']]
#     post_data = [r for d in [response['data'] for response in post_responses if 'data' in response] for r in
#                  d]  # flatten
#     posts = [d['message'] for d in post_data if 'message' in d]
#
#     return posts


## TODO get all pages of comments, make faster, maybe get the posts when they log in only and store?
def get_user_posts(access_token):
    '''    
    :param access_token: User access token
    :return: all the things that come from this person feed
    '''
    graph = facebook.GraphAPI(access_token)
    all_posts = []
    # for feed_type in ['statuses', 'posts']:
    posts = graph.get_object('me/feed')
    while posts['data']:
        try:
            # add the next page of user messages
            # add comments on these posts, including those made by friends
            all_posts += [post['message'] for post in posts['data'] if 'message' in post] + \
                         [comment['message'] for comment in
                          [post['comments'] for post in posts['data'] if 'comments' in post] if 'message' in comment]

            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            print "Key Error"
    return all_posts


def test():
    print get_user_posts(
        'CAAFiRqsaAxQBAJpCvKIkargA9MbD5LvUDPZBZC0L6IRGw4HikrqYSiqpLRLRTYDIL5SeQAhQZAqfpwPNZBVA2NtVbCZCFOK6tdZAyBUOtyvX7yPfwIj2INdIkgYOksfJ1ofSQdhXRz2ZBjJ2JFqIfvJJv1r5bteAdUSFDKhRlIwoVjXfB1IZAu4sIEuT06Yu7devZBY38umlc9NZC2JlEajweVZBpbpNY9ZBUAwZD'
    )


if __name__ == "__main__":
    test()