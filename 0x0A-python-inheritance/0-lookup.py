#!/usr/bin/python3
'''
Returns a list of available attributes and methods of an object
'''


def lookup(obj):
    '''
    Returns a list of available attributes and methods of an object
    '''
    return sorted(obj.__dir__(obj()))
