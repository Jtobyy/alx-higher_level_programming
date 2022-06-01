#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        if i >= 97 and i <= 122:
            print('{}'.format(chr(i - 32)), end='')
        else:
            print(c, end='')
    print()
