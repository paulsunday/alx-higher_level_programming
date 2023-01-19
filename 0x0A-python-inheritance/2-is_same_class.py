#!/usr/bin/python3
""" Defines a class-checking function."""


def is_same_class(obj, a_class):
    """ check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): THe class to match the type obj to.
    Returns:
        if obj is exactly an instance of a_class - True.
        otherwise - False.
    """
    if type(obj) == a_class:
        return True
    else:
        return False
