#!/usr/bin/python3
"""Defines a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""imported a method from a file """


class Rectangle(BaseGeometry):
    """This is a rectangle class that is a subclass of
    7-base_geometry, and inherits a method from it"""

    def __init__(self, width, height):
        """this is an init method that initializes the width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This is a string method that prints and return the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
