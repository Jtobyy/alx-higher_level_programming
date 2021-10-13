#!/usr/bin/python3
'''
Checks if an object is an instance of a specified
class
'''


def is_same_class(obj, a_class):
    '''
    Checks if an object is an instance of a specified
    class
    '''
    if isinstance(obj, a_class):
        if a_class == object:
            return False
        return True
    else:
        return False

