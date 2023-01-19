#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
	"""defines a txt file using the UTF-8 encoding format"""
	with open(filename, encoding="utf-8") as f:
	print(f.read())	
