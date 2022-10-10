#!/usr/bin/python3
"""
This module has a function that returns the python object
represented by  JSON string
"""
import json


def from_json_string(my_str):
    """ Returns the a python object represented by  JSON
    string"""
    return json.loads(my_str)
