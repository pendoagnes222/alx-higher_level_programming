#!/usr/bin/python3
"""
This module has a function that reads the txt file
and prints its contents to the stdout
"""


def read_file(filename=""):
    """Reads a txt file to the
    stdout
    Args:
        filename (str): file; default to empty string
    """
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        print(contents)
