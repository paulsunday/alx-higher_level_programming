#!/usr/bin/python3
"""Contains a function that returns a dict description
with simple data structure"""


def class_to_json(obj):
    """A function that returns dict
    description with simple data structure"""
    return obj.__dict__
