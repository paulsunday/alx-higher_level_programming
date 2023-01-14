#!/usr/bin/python3
""" This is aclass rectangle that has two parameter """

BaseGeometry = __import__("7-base_geometry.py").BaseGeometry


class Rectangle(BaseGeometry):
    """This is a Rectangle class that validates if the inputed numbers
    are integers that was inherited from a method (Base_geometry)
    in another file"""
    def __init__(self, width, height):
        """This method checks if the parameters are int"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
