#!/usr/bin/python3
"""
Contains a funtion that append to a file
"""


def append_write(filename="", text=""):
    """Defines a function that append to a file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
