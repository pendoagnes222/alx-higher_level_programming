#!/usr/bin/python3

"""
This module represents the base for any four sided shape
"""

from models.base import Base


class Rectangle (Base):
    """This is a Rectangle class
    Attributes:
    id: id of object
    width: width of the rectangle
    height: height of the rectangle
    x: x coordinate of rectangle
    y: y coordinate of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of width
        """
        self.__width = self.validate('width', value)

    @property
    def height(self):
        """
        Get Value of __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of private instance variable __height
        """
        self.__height = self.validate('height', value)

    @property
    def x(self):
        """
        Get value of __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets Value of __x
        """
        self.__x = self.validate('x', value)

    @property
    def y(self):
        """
        Gets Value of private instance variable __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets the value of __y
        """
        self.__y = self.validate('y', value)

    def validate(self, prop, val):
        """
        This is a helper class for validating
         inputs to private instance attributes
        """

        if(type(val) is not int):
            raise TypeError('{} must be an integer'.format(prop))
        if (prop in ['x', 'y'] and val < 0):
            raise ValueError('{} must be >= 0'.format(prop))
        elif (prop in ['height', 'width'] and val <= 0):
            raise ValueError('{} must be > 0'.format(prop))
        return val

    def area(self):
        """
        Computes the area
        """
        return self.width * self.height

    def display(self):
        """
        This prints the rectangle to the
        Terminal
        """
        print('\n' * (self.__y), end='')
        for i in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Returns the informal representation of the object"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        This updates class instance attributes
            Args:
                *args:Tuple of variables
                **kwargs: A dictionary of variables
        """
        prop = ['id', 'width', 'height', 'x', 'y']
        len_args = len(args)
        if len_args > 0:
            [setattr(self, prop[i], args[i]) for i in range(len_args)]
        else:
            [setattr(self, k, v) for k, v in kwargs.items() if k in prop]

    def to_dictionary(self):
        """
        This returns a dictionary of class attributes
        """
        prop = ['id', 'width', 'height', 'x', 'y']
        dict_ = {}
        for i in prop:
            dict_[i] = getattr(self, i)
        return dict_
