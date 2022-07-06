#!/usr/bin/python3
"""
Module that has a function that returns a dictionary with simple
data structure for JSON serialization of an object
"""


def class_to_json(obj):
    """Returns a dictionary with simple data structures
    for JSON serialization of an object
    """
    return obj.__dict__
