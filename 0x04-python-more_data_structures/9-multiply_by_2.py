#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    for k, v in a_dictionary.items():
        new_dict[k] = v
    for k, v in new_dict.items():
        new_dict[k] *= 2
    return new_dict
