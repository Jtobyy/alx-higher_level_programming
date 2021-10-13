#!/usr/bin/python3
'''
writes a string to a text file
'''


def write_file(filename="", text=""):
    '''
    writes a string to a text file(UTF8) and return the number
    of characters written
    '''
    with open(filename, 'w+', encoding='utf-8') as t:
        n = t.write(text)
    return n
