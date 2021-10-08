#!/usr/bin/python3
'''
extended version of 5-base_geometry
'''


class BaseGeometry:
    '''
    base geometry class
    '''
    def area(self):
        '''
        raises an exception
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        validates a value
        '''
