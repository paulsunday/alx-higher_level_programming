#!/usr/bin/python3
"""contains a class studdent"""


class Student:
    """Repr a student class"""
    def __init__(self, first_name, last_name, age):
        """Initialization of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """returns a dictionary repre of a student instance
        with specific attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attr of a student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
