#!/usr/bin/python3
""" This is a BaseGeometry class"""


class BaseGeometry:
    def area(self):
        """This is a function that raise an exception error
        if the area of the class is not defined
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This function validates value and raise a type error
        if the value is not int or
        value error if value is less than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
