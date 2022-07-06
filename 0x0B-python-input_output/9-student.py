#!/usr/bin/python3
"""
A module containing a class
"""


class Student():
    """
    A Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of class attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
