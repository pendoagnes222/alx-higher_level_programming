#!/usr/bin/python3

"""This is the "0-add_integer" module
The 0-add_integer module supplies one function, add_integer()
"""


def add_integer(a, b=98):
    """
    Sums two integers a and b together. b defaults to 98
    """
    if type(a) not in [float, int]:
        raise TypeError('a must be an integer')
    if type(b) not in [float, int]:
        raise TypeError('b must be an integer')
    return int(round(a+b))
