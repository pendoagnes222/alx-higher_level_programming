#!/usr/bin/python3
"""Module to create a Rectangle Object
"""


class Rectangle:
    """This is Rectangle class
    """

    def __init__(self, width=0, height=0):
        """This is __init__ method
        Is to initialize variables
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        for i in range(self.__height):
            result += "#" * self.__width
            if (i != self.__height - 1):
                result += "\n"
        return result

    def __repr__(self):
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        print("Bye rectangle...")
