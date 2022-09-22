#!/usr/bin/python3

def islower(c):
    '''checks for lower case characters and returns true if lower'''
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
