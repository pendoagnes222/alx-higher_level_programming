#!/usr/bin/python3
"""Creates a square class"""


class Square():
    """
    Define a square
    """
    def __init__(self, size=0):
        """
        size initialization.
        Args:
            size: integer value
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
