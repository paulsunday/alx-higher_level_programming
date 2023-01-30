#!/usr/bin/python3
"""Contains a class called Base"""


class Base:
    """Class base for other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is an init method"""
        if id is not iNone:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_obects
