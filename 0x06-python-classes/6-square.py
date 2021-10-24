#!/usr/bin/python3
"""defines a square by: (based on 0-square.py)"""


class Square:
    """defines a square by: (based on 0-square.py)"""
    def __init__(self, size=0, position=(0, 0)):
        """defines a private attribute of the class"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, val):
        if not isinstance(val, int):
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    @position.setter
    def position(self, value):
        if not isinstance(value, turple):
            raise TypeError("position must be a turple \
            of two positive integers")
        else:
            for i in value:
                if not isinstance(i, int) or i < 0:
                    raise TypeError("position must be a turple \
                    of two positive integeres")
            self.__postion = value

    def area(self):
        x = self.size**2
        return x

    def my_print(self):
        if self.size == 0:
            print()
        for v in range(self.position[1]):
            print()
        for i in range(self.size):
            for h in range(self.position[0]):
                print('_', end="")
            for i in range(self.size):
                print('#', end="")
            print()
