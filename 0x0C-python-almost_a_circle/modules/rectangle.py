
#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """ class for the rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializing attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """ getter and setter for width """
    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        self.validate("width", value)
        self.__width = value

    """ getter and setter for height """
    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        self.validate("height", value)
        self.__height = value

    """ getter and setter for x """
    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        self.validate("x", value)
        self.__x = value

    """ getter and setter for y """
    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y """
        self.validate("y", value)
        self.__y = value

    def validate(self, name, value):
        """ validates the given inputs """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if name in ["width", "height"] and value <= 0:
            raise ValueError("{:s} must be > 0".format(name))
        if name in ["x", "y"] and value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def area(self):
        """ returns the area value of the Rectangle instance """
        return (self.height * self.width)

    def display(self):
        """ prints in stdout the Rectangle instance with character # """
        for n in range(self.y):
            print()
        for index in range(self.height):
            print("".join(" " for j in range(self.x)), end="")
            print("".join(["#" for k in range(self.width)]))

    def __str__(self):
        """ overides the string method """
        ret = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return (ret.format(self.id, self.x, self.y, self.width, self.height))
