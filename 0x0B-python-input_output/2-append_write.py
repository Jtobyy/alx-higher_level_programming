#!/usr/bin/python3
'''
Appends a string at the end of text file
'''


def append_write(filename="", text=""):
    '''
    Appends a string at the end of text file
    '''
    with open(filename, 'a+') as f:
       n = f.write(text) 
    return n
