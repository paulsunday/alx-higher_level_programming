#!/usr/bin/python3
"""
This is a class that defines an area inherited from another class
"""


class BaseGeometry:
    """Raise an Exception on the area attribute"""
    def area(self):
        raise Exception("area() is not implemented")
