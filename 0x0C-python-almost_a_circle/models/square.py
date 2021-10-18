#!/usr/bin/python3
'''Defines the Square class that inherits from Rectangle'''
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    '''class Square inherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''initialization actions'''
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        '''override the __str__ method of a class'''
        str_ = f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'
        return (str_)

    @property
    def size(self):
        '''getter property for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size'''
        if not isinstance(value, int):
                raise TypeError("width must be an integer")
        elif value <= 0:
                raise ValueError("width must be > 0")
        else:
                self.__size = value

    def update(self, *args, **kwargs):
        '''Updates the class - Square by assigning an argument
        to each attribute'''
        args_len = len(args)
        if args_len >= 1:
            if args_len == 1:
                self.id = args[0]
            elif args_len == 2:
                self.id = args[0]
                self.size = args[1]
            elif args_len == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
            elif args_len == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''returns the dictionary representation of a Square'''
        dict_ = {'size': self.size, 'x': self.x,
                 'y': self.y, 'id': self.id}
        return dict_
