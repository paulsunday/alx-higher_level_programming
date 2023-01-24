#!/usr/bin/python3
"""contains a function that writes an obj
to a txt file"""

import json


def save_to_json_file(my_obj, filename):
    """Saves json representation to file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
