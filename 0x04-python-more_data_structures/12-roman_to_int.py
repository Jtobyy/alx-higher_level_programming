#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    idx = 0
    while (idx < len(roman_string) - 1):
        c = roman_string[idx]
        d = roman_string[idx + 1]
        val1 = get_val_from_dict(dict, c)
        val2 = get_val_from_dict(dict, d)
        if val1 >= val2:
            number += val1
            idx += 1
        elif c < d:
            number += (val2 - val1)
            idx += 2
    if idx < len(roman_string):
        val = get_val_from_dict(dict, roman_string[len(roman_string) - 1])
        number += val
    return number


def get_val_from_dict(dict, key):
    for k, v in dict.items():
        if k == key:
            return dict[key]
