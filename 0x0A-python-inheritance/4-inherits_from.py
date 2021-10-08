#!/usr/bin/python3
'''
Checks if the object is an instance of a
class that inherited from the specified class
'''


def inherits_from(obj, a_class):
    '''
    Checks if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class
    '''

    if isinstance(obj, a_class):
        if type(obj) == a_class:
            return False
        return True
    else:
        return False
