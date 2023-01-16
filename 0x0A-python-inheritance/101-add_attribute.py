#!/usr/bin/python3
"""Defines a new attribute"""


def add_attribute(obj, attr_name, attr_val):
    """an attribut/funtion/object/method"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, attr_val)
    else:
        raise TypeError("can't add new attribute")
