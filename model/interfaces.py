__author__ = 'jatwood'

class Corpus:
    '''
    A Corpus represents a collection of text.

    The Corpus manages the storage and processing of text from different sources,
    and also provides iterators over processed text.
    '''

    def __init__(self, sources=[]):
        self.sources = sources

    def __iter__(self):
        pass

class Source:
    '''
    A Source provides an interface to a particular text source while managing storage.
    '''

    def __init__(self):
        pass

    def __iter__(self):
        pass


class SourceProcessor:
    '''
    A SourceProcessor manages the storage and computation of a text transformation on a particular Source.
    '''

    def __init__(self):
        pass

    def process(self):
        pass


class Processor:
    '''
    A Processor computes a text transformation.
    '''

    def __init__(self):
        pass

    def __apply__(self, *args):
        if len(args) == 1:
            self.process(args)

    def process(self):
        pass

class Pipeline:
    '''
    A Pipeline composes Processors into a chain of operations.
    '''

    def __init__(self,processors):
        self.processors = processors


class Model:
    '''
    A Model learns from a Corpus to produce new text.
    '''

    def __init__(self, corpus):
        self.corpus = corpus






