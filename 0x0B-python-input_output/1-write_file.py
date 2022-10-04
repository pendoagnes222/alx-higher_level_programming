#!/usr/bin/python3
"""
This module has a function that writes a string to a text file
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns
    the number of characters written"""
    with open(filename, 'w', encoding='utf-8') as f:
        content = f.write(text)
        return content
