#!/usr/bin/python3
"""defines a square by: (based on 0-square.py)"""


class Square:
    """defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0):
        """defines a private attribute of the class"""
        self.__set_size(size)

    def __get_size(self):
        return self.__size

    def __set_size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val
