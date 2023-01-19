#!/usr/bin/python3
"""
This is a function that checks if an obj is
an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    The function takes in 2 arguments, the first is the obect of the class,
    while the second id the class.
    it then checks if the object is a kind of the class
    and returns a bool value
    """

    return isinstance(obj, a_class)
