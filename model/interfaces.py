__author__ = 'jatwood'

class Corpus:
    '''
    A Corpus represents a collection of text.

    The Corpus manages the storage and processing of text from different sources,
    and also provides iterators over processed text.
    '''

    def __iter__(self):
        raise NotImplementedError

class Source:
    '''
    A Source provides an interface to a particular text source while managing storage.
    '''

    def __iter__(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError


class SourceProcessor:
    '''
    A SourceProcessor manages the storage and computation of a text transformation on a particular Source.
    '''

    def process(self):
        raise NotImplementedError


class Processor:
    '''
    A Processor computes a text transformation.
    '''
    def __apply__(self, *args):
        if len(args) == 1:
            self.process(args)

    def process(self):
        raise NotImplementedError

class Pipeline:
    '''
    A Pipeline composes Processors into a chain of operations.
    '''

    def __init__(self,processors):
        raise NotImplementedError


class Model:
    '''
    A Model learns from a Corpus to produce new text.
    '''

    def learn(self):
        raise NotImplementedError

    def generate(self):
        raise NotImplementedError







