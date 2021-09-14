#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    b_dictionary = sorted(a_dictionary)
    for val in b_dictionary:
        for k, v in a_dictionary.items():
            if k == val:
                dic = f'{k}: {v}'
                print("{}".format(dic))
