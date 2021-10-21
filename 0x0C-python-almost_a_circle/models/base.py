#!/usr/bin/python3
"""Base class for other shapes"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        ret_list = []
        filename = cls.__name__ + ".json"
        with open(filename, "w+") as f:
            for instance in list_objs:
                dict_ = instance.to_dictionary()
                ret_list.append(dict_)
            f.write(Base.to_json_string(ret_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return "[]"
        else:
            ret_obj = json.loads(json_string)
            return ret_obj
