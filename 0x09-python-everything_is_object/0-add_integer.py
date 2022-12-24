#!/usr/bin/python3
def add_integer(a, b=98):
    """ This function adds 2 integers"""
    if a == float:
        a = int(a)
    if b == float:
        b = int(b)
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(a) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    return a + b
