#!/usr/bin/python3
"""
The function returns true uf the object is an istance of a class
that nherited (directly or indirectly) from the specified class
otherwise false
"""


def inherits_from(obj, a_class):
    """
    The function takes two arguments obj and a class, and it checks
    if the object is of the same kind with the class and the type of the object
    is not exactly equal to the class
    """

    return isinstance(obj, a_class) and not type(obj) == a_class
