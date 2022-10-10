#!/usr/bin/python3
"""
This module has a function that writes an object to
a txt file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a txt file
    using JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json_obj = json.dumps(my_obj)
        f.write(json_obj)
