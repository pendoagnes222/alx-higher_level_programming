#!/usr/bin/python3
"""
This module represents the base class for all
subsequent classes in this package
"""


import json
import os.path
import csv


class Base:
    """
    This class represents the base for subsequent classes
    in this project
    Attributes:
     __nb_objects: this represents the unique object id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is called when a new instance of Base is created
            Args:
                id : is used to manage attributes and aboid creating same code
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def reset_objects():
        """Resets number of objects for testing"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This converts list of dictionaries to json string
        Args:
            list_dictionaries: This is the list of dictionary to convert
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves list of objects of type cls to a file
        Args:
            cls: This is the class type to be saved
            list_objs: This is the list of instances
        """
        list_cls = []
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as fp:
            if list_objs is not None:
                [list_cls.append(i.to_dictionary()) for i in list_objs]
            fp.write(cls.to_json_string(list_cls))

    @staticmethod
    def from_json_string(json_string):
        """
        This converts a list representing list of dictionaries
        to a json string
        Args:
            json_string: This is the string representing a list of dictionaries
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This creates an instance of a class cls from
        a dictionary
        Args:
            cls: This is the class type to be intanced
            **dictionary: This is the dictionary containing class variables
        """
        if cls.__name__ == 'Rectangle':
            n = cls(1, 1)
            n.update(**dictionary)
            return n
        elif cls.__name__ == 'Square':
            n = cls(1)
            n.update(**dictionary)
            return n

    @classmethod
    def load_from_file(cls):
        """
        This loads a class instance from a json file
        Args:
            cls : The class type to load into
        """
        file_name = cls.__name__ + '.json'
        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as fp:
                ls_str_instance = Base.from_json_string(fp.read())
                ls_rl_instances = []
                for i in ls_str_instance:
                    ls_rl_instances.append(cls.create(**i))
                return ls_rl_instances
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        This saves list of class intance of type cls as csv
        Args:
            cls: Class type
            list_objs: This is a list of class instances
        """
        file_name = cls.__name__ + '.csv'
        if file_name == 'Rectangle.csv':
            field_names = ['id', 'width', 'height', 'x', 'y']
        else:
            field_names = ['id', 'size', 'x', 'y']
        with open(file_name, 'w', encoding='utf-8') as fp:
            csv_w = csv.DictWriter(fp, fieldnames=field_names)
            csv_w.writeheader()
            for i in list_objs:
                if list_objs is not None:
                    csv_w.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        This loads list of class intance of type cls as csv
        Args:
            cls: Class type
        """
        file_name = cls.__name__ + '.csv'
        list_objs = []
        with open(file_name, 'r') as fp:
            csv_r = csv.DictReader(fp)
            for i in csv_r:
                for k, v in i:
                    i[k] = int(v)
                list_objs.append(cls.create(**i))
