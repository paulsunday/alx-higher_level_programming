#!/usr/bin/python3
""" This class defines a locked class"""
class LockedClass:
    """
    prevents the user from instantiating a new LockedClass
    attributes for anything but attributes alled 'first_name' using 
    slot which is used to specify a fixed attribute
    """

    __slot__ = ["first_name"]
