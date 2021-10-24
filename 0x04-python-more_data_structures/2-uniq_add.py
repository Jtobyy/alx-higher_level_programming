#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    uniq = []
    for i in my_list:
        for j in uniq:
            if i == j:
                break
        else:
            result += i
            uniq.append(i)
    return result
