#!/usr/bin/python3
"""Contains a function that returns the JASON rep"""

import json


def to_json_string(my_obj):
    """Returns a json rep of a string"""
    return json.dumps(my_obj)
