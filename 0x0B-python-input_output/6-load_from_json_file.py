#!/usr/bin/python3
"""Contains a function that creates an obj
from a json file"""

import json


def load_from_json_file(filename):
    """Defines a function that creates an obj ffrom json file"""
    with open(filename, encoding="utf-8") as f:
        the_json_data = json.load(filename)
    return the_json_data
