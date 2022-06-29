#!/usr/bin/python3
"""
Module that has the function text_indentation
"""

def text_indentation(text):
    """Prints a text with 2 lines after '.', '?' and ':'
    Args:
        text (str): collection of strings and special characters
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    i = 0
    start = 0
    while text[i < len(text)]:
        if i >= len(text):
            break
        for character in ['.', '?', ':']:
            if text[i] == character:
                print(f'{text[start:i]}{character}\n')
                start = i + 2
        i += 1
    print(text[start:], end="")
