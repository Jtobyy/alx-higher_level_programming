#!/usr/bin/python3
"""Base class for other shapes"""
import json
import turtle


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
            if (list_objs == None):
                f.write(Base.to_json_string(None))
                return
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

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 4)
        elif cls.__name__ == 'Square':
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        list_of_instances = []
        filename = cls.__name__+".json"
        with open(filename, 'r') as f:
            instance_ = f.read()
            obj = cls.from_json_string(instance_)
            for instance in obj:
                obj_copy = cls.create(**instance)
                list_of_instances.append(obj_copy)
        return list_of_instances

    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__+".csv"
        with open(filename, "w+") as f:
            pass
            
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__+".csv"
        with open(filename, "w+") as f:
            pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
            my_turtle = turtle.Turtle()
            window.mainloop()
        for rectangle in list_rectangles:
            forward(rectangle.width)
            right(90)
            forward(rectangle.height)
            left(90)
            forward(rectangle.width)
            right(90)
            forward(rectangle.width)
        
        for square in list_squares:
            forward(square.width)
            right(90)
            forward(square.height)
            left(90)
            forward(square.width)
            right(90)
            forward(square.height)
            
