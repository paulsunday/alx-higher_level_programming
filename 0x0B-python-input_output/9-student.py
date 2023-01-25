#!/usr/bin/python3
"""Defines a class that defines a student"""


class Student:
    """Has a public instance that has
    first name, last name and age of the student"""

    def __init__(self, first_name, last_name, age):
        """The public inistialization of the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A public method that retrives a dict repr of a student"""
        return self.__dict__
