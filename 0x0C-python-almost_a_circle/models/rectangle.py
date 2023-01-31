#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
"""
    Class Rectangle used to define a rectangle
    ...
    Attributes
    ----------
    width : int
        the width of the rectangle
    height : int
        height of the rectangle
    x : int
        x coordinate
    y : int
        y coordinate
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor to initialize instances"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
