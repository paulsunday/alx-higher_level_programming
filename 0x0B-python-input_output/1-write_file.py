#!/usr/bin/python3
"""

def write_file(filename="", text=""):
    """Write a file with the keyword"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
