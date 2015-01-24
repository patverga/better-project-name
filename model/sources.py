__author__ = 'jatwood'

import model.interfaces as interfaces

class FacebookSource(interfaces.Source):
    def __init__(self, username):
        self.username = username

