#!/usr/bin/python3
"""Contains a function that returns a dict description
with simple data structure"""
import json


def class_to_json(obj):
    return json.loads(json.dumps(obj, default=lambda o: o.__dict__))
