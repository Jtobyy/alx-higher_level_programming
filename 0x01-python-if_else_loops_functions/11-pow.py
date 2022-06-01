#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b < 0:
        i = 0 - b
    else:
        i = b
    for i in range(i):
        p *= a
    if b < 0:
        return 1/p
    else:
        return p
