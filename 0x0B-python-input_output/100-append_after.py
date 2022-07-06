#!/usr/bin/python3
"""
append string
"""


def append_after(filename="", search_string="", new_string=""):

    """
    Append string
    Args:
        filename(str): file name
        search_string: string to be replaced
        new_string: string to replace
    """
    ls = []
    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            if search_string in line:
                ls.append(line)
                ls.append(new_string)
            else:
                ls.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(ls))
