import facebook
import requests

__author__ = 'pv'


# def get_user_posts(access_token):
# """
#     get all the posts and status updates this user has made
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


# def all_user_posts(access_token, user_name):
def get_user_posts(access_token):
    graph = facebook.GraphAPI(access_token)
    all_posts = []
    # for feed_type in ['statuses', 'posts']:
    posts = graph.get_object('me/feed')
    while posts['data']:
        try:
            all_posts += [post['message'] for post in posts['data'] if 'message' in post]
            all_posts += [comment['message'] for comment in
                          [post['comments'] for post in posts['data'] if 'comments' in post] if 'message' in comment]

            # grab each post/status text
            # if 'message' in post:
            #     all_posts.append(post['message'])
            # get all the comments by this user
            # if 'comments' in post:
            #     all_posts.append(all_post_comments(post, user_name))
            # get all pages of results
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            print "Key Error"
    return all_posts


def all_post_comments(post, user_name):
    user_comments = []
    comments = post['comments']
    while comments['data']:
        try:
            for comment in comments['data']:
                # grab if this user wrote it
                if 'from' in comment and 'name' in comment['from'] and user_name is comment['from']['name']:
                    user_comments.append(comment['message'])
            # get all pages of results
            comments = requests.get(comments['paging']['next']).json()
        except KeyError:
            print "Key Error"
    return user_comments


def test():
        print get_user_posts(
            'CAAFiRqsaAxQBAJpCvKIkargA9MbD5LvUDPZBZC0L6IRGw4HikrqYSiqpLRLRTYDIL5SeQAhQZAqfpwPNZBVA2NtVbCZCFOK6tdZAyBUOtyvX7yPfwIj2INdIkgYOksfJ1ofSQdhXRz2ZBjJ2JFqIfvJJv1r5bteAdUSFDKhRlIwoVjXfB1IZAu4sIEuT06Yu7devZBY38umlc9NZC2JlEajweVZBpbpNY9ZBUAwZD'
        )

if __name__ == "__main__":
    test()