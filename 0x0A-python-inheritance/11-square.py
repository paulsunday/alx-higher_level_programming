#!/usr/bin/python3
"""Defines a class Rectangle"""


Rectangle = __import__("9-rectangle").Rectangle
"""This imports the method Rectangle from a file"""


class Square(Rectangle):
    """Defines a class Square with a method
    that inherits method from other class"""

    def __init__(self, size):
        """This method calls super and validate if the
        size is integer"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Defines the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """This method prints the the square decscription"""
        return "[Square] {}/{}".format(self.__size, self.__size)
