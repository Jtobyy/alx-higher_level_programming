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
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
