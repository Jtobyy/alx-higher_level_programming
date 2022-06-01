#!/usr/bin/python3
def uppercase(str):
    sen = ''
    for c in str:
        i = ord(c)
        if i >= 97 and i <= 122:
            sen += chr(i - 32)
        else:
            sen += chr(i)
    print('{}'.format(sen))
