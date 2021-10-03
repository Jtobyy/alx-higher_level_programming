#!/usr/bin/python3
"""oop rectangle practice

   >>> Rectangle
   <class '__main__.Rectangle'>
"""


class Rectangle:
    """
    defines a Rectangle
    
    >>> my_rectangle = Rectangle()
    >>> print(type(my_rectangle))
    <class '__main__.Rectangle'>
    >>> print(my_rectangle.__dict__)
    {}
    """
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()


