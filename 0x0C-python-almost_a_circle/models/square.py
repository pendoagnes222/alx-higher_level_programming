#!/usr/bin/python3
"""
This module represents a Sqauare
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a Square class
    Attributes:
    id: id of object
    size: this is the size of square
    x: x coordinate of rectangle
    y: y coordinate of rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of Square class"""
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """
        This returns the string representation of sqaure class
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """
        Gets the size
        """
        return self.height

    @size.setter
    def size(self, value):
        """
        This sets the size of the square
        Args:
            value: Value to set
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        This updates class instance attributes
            Args:
                *args:Tuple of variables
                **kwargs: A dictionary of variables
        """
        prop = ['id', 'size', 'x', 'y']
        len_args = len(args)
        if len_args > 0:
            for i in range(len_args):
                if type(args[i]) == int:
                    setattr(self, prop[i], args[i])
        else:
            for k, v in kwargs.items():
                if k in prop and type(v) == int:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        This returns a dictionary of class attributes
        """
        prop = ['id', 'size', 'x', 'y']
        dict_ = {}
        for i in prop:
            dict_[i] = getattr(self, i)
        return dict_
