#!/usr/bin/python3
"""Contains a class called Base"""
import json
import csv
import os.path


class Base:
    """Class base for other classes"""
    self.__nb_objects = 0

    def __init__(self, id=None):
        """This is an init method"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_obects
