#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """This reperensents a circle"""
    def __int__(self, radius=0):
        """Initializes the magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of the circle"""
        return 2 * math.pi * self.__radius
