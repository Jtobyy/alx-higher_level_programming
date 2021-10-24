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
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (2*self.height + 2*self.width)

    def __str__(self):
        rect = []
        if self.height == 0 or self.width == 0:
            return ""
        for h in range(self.height):
            for w in range(self.width):
                rect.append('#')
            rect.append("\n")
        rect.pop()
        rect_str = ''.join([str(item) for item in rect])
        return rect_str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print ("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
