#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val_list = []
    for k, v in a_dictionary.items():
        val_list.append(v)
    b = 0
    i = 0
    while (i < len(val_list)):
        if val_list[i] > b:
            b = val_list[i]
        i += 1
    for k, v in a_dictionary.items():
        if v == b:
            return k
    else:
        return None
