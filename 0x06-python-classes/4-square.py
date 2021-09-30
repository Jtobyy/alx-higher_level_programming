#!/usr/bin/python3
"""defines a square by: (based on 0-square.py)"""


class Square:
    """defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0):
        """defines a private attribute of the class"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    def area(self):
        x = self.size**2
        return x
