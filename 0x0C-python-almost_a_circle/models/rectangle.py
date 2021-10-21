#!/usr/bin/python3
"""Defines the Rectangle class"""
from base import Base


class Rectangle(Base):
    """Rectangle class inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization actions"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
 
    @property
    def width(self):
        """getter property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
                raise TypeError("width must be an integer")
        elif value <= 0:
                raise ValueError("width must be > 0")
        else:
                self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
                raise TypeError("height must be an integer")
        elif value <= 0:
                raise ValueError("height must be > 0")
        else:
                self.__height = value
   
    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
                raise TypeError("x must be an integer")
        elif value < 0:
                raise ValueError("x must be >= 0")
        else:
                self.__x = value
            
    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if not isinstance(value, int):
                raise TypeError("y must be an integer")
        elif value < 0:
                raise ValueError("y must be >= 0")
        else:
                self.__y = value
            
    def area(self):
        """Calculate the area of a Rectangle instance"""
        return (self.height * self.width)

    def display(self):
        """Display the instance using #"s"""
        rect = []
        for y in range(self.y):
            rect.append("\n")
    
        for h in range(self.height):
            for x in range(self.x):
                rect.append(" ")
            for w in range(self.width):
                rect.append("#")
            rect.append("\n")
        rect.pop()
        rect_str = "".join([str(item) for item in rect])
        print(rect_str)

    def __str__(self):
        """override the __str__ method of a class"""
        str_ = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return (str_)

    def update(self, *args, **kwargs):
        """Updates the class Rectangle by assigning an argument
        to each attribute"""
        args_len = len(args)
        if args_len >= 1:
            if args_len == 1:
                self.id = args[0]
            elif args_len == 2:
                self.id = args[0]
                self.width = args[1]
            elif args_len == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            elif args_len == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            elif args_len == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        dict_ = {"width": self.width, "height": self.height, "x": self.x,
                 "y": self.y, "id": self.id}
        return dict_
