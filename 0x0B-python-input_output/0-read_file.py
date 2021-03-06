#!/usr/bin/python3
'''
reads a text and prints it out
'''


def read_file(filename=""):
    '''
    reads a text(UTF8) and prints it out
    '''

    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
    return
