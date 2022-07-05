#!/usr/bin/python3
"""Module: 100-my_int.
Defines a class that inherits from int.
"""


class MyInt(int):
    """MyInt inheriting from int
    and alters the behaviour of __eq__ and
    __ne__ methods
    """

    def __eq__(self, other):
        """Equal to returns not equal to."""

        return super().__ne__(other)

    def __ne__(self, other):
        """Not equal to returns equal to."""

        return super().__eq__(other)
