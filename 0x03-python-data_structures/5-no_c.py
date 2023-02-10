#!/usr/bin/python3


def no_c(my_string):
    copy = ''
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        copy += c
    my_string = copy
    return my_string
