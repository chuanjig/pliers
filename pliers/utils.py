import collections
from six import string_types

def listify(obj):
    ''' Wraps all non-list or tuple objects in a list; provides a simple way
    to accept flexible arguments. '''
    return obj if isinstance(obj, (list, tuple, type(None))) else [obj]

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, string_types):
            for sub in flatten(el):
                yield sub
        else:
            yield el