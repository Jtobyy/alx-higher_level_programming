#!/usr/bin/python3

def multable():
    table = []
    for i in range(1, 10):
        subtable = [i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9]
        print("{}".format(subtable))
        print()       
        table.append(subtable)
    return table

multable()

