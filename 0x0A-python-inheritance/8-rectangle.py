#!/usr/bin/python3
'''
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Rectangle Class that inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
