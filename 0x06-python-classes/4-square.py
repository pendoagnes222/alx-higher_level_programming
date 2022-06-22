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

    def area(self):
        """
        calculate area of square
        """
        return self.__size**2

    @property
    def size(self):
        """
        return size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set size of square
        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
