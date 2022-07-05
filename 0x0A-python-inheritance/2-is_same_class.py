#!/usr/bin/python3
"""This module contains a function that returns True if an object is
exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """Determines if the object is an instance of the specified class
    Args:
        obj: object
        a_class: Classs
    """
    if type(obj) == a_class:
        return True
    return False
