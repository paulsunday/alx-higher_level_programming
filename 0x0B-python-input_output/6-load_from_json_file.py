#!/usr/bin/python3
"""Contains a function that creates an obj
from a json file"""

import json


def load_from_json_file(filename):
    """Defines a function that creates an obj ffrom json file"""
    with open(filename) as f:
        json.load(filename)
