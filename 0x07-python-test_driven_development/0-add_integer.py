#!/usr/bin/python3
"""
Function that does addition and subtraction
"""
def add_integer(a, b=98):
    """ A and B must be int or float
    else raise error msg
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError ("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError ("b must be an integer")
    elif type(a) is float:
        int = int(a)
    elif type(b) is float:
        int = int(b)
    return a + b

