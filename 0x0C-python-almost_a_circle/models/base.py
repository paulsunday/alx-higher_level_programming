#!/usr/bin/python3
"""Module for base class"""
import json
import csv
import os.path


class Base:
    """Base class for all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
