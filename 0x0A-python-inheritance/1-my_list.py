#!/usr/bin/python3
""" 
Module: 1-my_list
"""

class MyList(list):
    """ Represents a MyList """

    def print_sorted(self):
        """ Prints the list, but sorted """

        print(sorted(self))
