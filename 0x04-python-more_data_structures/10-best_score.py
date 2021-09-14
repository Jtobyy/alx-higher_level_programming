#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    val_dict = []
    for k, v in a_dictionary.items():
        val_dict.append(v)
    i = 1
    while (i < len(val_dict)):
        if val_dict[i] > val_dict[i-1]:
            b = val_dict[i]
        else:
            b = val_dict[i-1]
        i += 1
    for k, v in a_dictionary.items():
        if v == b:
            return k
    else:
        return None
