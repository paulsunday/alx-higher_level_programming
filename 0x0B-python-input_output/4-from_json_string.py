#!/usr/bin/python3
"""Contains a function that returns an object
rep by a Json"""


def from_json_string(my_str):
    """Returns an object using jason loads"""
    return json.loads(my_str)
