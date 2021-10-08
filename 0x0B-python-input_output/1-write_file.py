#!/usr/bin/python3
'''
writes a string to a text file
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file(UTF8) and return the number
    of characters written
    '''
    with open(text, 'w') as t:
        with open(filename, 'r') as f:
            n = t.write(f.read())
    return n

