#!/usr/bin/python3
'''
prints a text with 2 new lines after each
of characters '.', '?' and ':'
'''


def text_indentation(text):
    '''
    prints a text with 2 new lines after each
    of the characters '.', '?' and ':'
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    text_len = len(text)
    while i < text_len:
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print()
            print()
            i += 1
            while text[i] == " " and i < (text_len - 2):
                i += 1
        else:
            i += 1
