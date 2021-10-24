#!/usr/bin/python3

def common_elements(set_1, set_2):
    common_set = []
    for i in set_1:
        common_set += filter(lambda x: x == i, set_2)
    return common_set
