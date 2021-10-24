#!/usr/bin/python3
'''prints a square with the character #'''


def print_square(size):
    '''prints a square with the character #'''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for s in range(size):
        for s in range(size):
            print('#', end="")
        print()
