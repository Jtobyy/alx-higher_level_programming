#!/usr/bin/python3
'''
Adds two integers and returns their sum
'''


def add_integer(a, b=98):
    '''
    return the sum of integers a and b
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
