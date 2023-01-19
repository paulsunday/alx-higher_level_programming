#!/usr/bin/python3
"""Defines a class that inherits from a built in method"""


class MyInt(int):
    """This is a class and its inherited method"""
    def __eq__(self, other):
        """Calls the built in equality method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Calls the not equal built in method"""
        return super().__eq__(other)
