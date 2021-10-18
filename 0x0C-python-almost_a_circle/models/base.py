#!/usr/bin/python3
'''Base class for other shapes'''
import json


class Base:
    '''Base class'''
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
        '''writes the JSON string representation of list_objs to a file'''
        print(cls.__name__)
        filename = cls.__name__ + '.json'
        with open(filename, 'w+') as f:
            dict_ = cls.to_dictionary()
            f.write(to_json_string(dict_))
