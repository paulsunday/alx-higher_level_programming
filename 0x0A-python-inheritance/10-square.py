#!/usr/bin/python3
"""Defines a class Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle
"""Imported from a file"""


class Square(Rectangle):
    """The class Rectangle. can this be called an object?"""
    def __init__(self, size):
        """AN init methed that validates if it is an integer
        and it calls the parent class with the super method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Defines the area of the rectangle"""
        return self.__size ** 2
