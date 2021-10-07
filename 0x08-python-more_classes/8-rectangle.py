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

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
                rect.append(Rectangle.print_symbol)
            rect.append("\n")
        rect.pop()
        rect_str = ''.join([item for item in rect])
        return rect_str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    def __del__(self):
        type(self).number_of_instances -= 1
        print ("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
