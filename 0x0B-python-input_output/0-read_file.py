#!/usr/bin/python3
"""
This module has a function that reads the text file
and prints its contents to the stdout
"""


def read_file(filename=""):
    """Reads a text file to the
    stdout
    """
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        print(contents, end='')
