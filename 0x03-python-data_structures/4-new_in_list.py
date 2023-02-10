#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copy = list(my_list)
    if idx < 0:
        return copy
    elif idx >= len(copy):
        return copy
    copy[idx] = element
    return copy
