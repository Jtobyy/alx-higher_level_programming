#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(-3, -3)
print(my_rectangle.__dict__)

my_rectangle.width = 2
my_rectangle.height = 3
print(my_rectangle.__dict__)
