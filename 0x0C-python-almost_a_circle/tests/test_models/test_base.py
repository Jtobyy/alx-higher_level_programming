#!/usr/bin/python3
'''
Test suite for base
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_get_id(self):
        '''.....'''
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        self.assertEqual(Base().id, 5)
        
    def test_get_private_attr(self):
        '''.....'''
        with self.assertRaises('AttributeError'):
            b6 = Base()
            b1.nb_objects
        with self.assertRaises('AttributeError'):
            b6.__nb_objects
        with self.assertRaises('AttributeError'):
            b6.__nb_objects = 2
            
    def test_to_json_string(self):
        '''Test method to_json_string that returns the JSON
        string representation of list_dictionaries'''
        b7 = base(8)
        self.assertEqual(b7.to_json_string(None), '[]')
        self.assertEqual(b7.to_json_string(), '[]')
        self.assertEqual(b7.to_json_string(None), '[]')

        r1 = Rectangle(10, 7, 2, 8, id=1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(print(sorted(dictionary)), {'height': 7, 'id': 1, 'x': 2,
                                                     'width': 1, 'y': 8})
        self.assertEqual(print(type(dictionary)), "<class 'dict'>")
        self.assertEqual(print(sorted(json_dictionary)), [{"height": 7, "id": 1,
                                                        "x":2, "width": 1, "y": 8}])
        self.assertEqual(print(type(json_dictionary)), "<class 'str'>")
      
    def test_save_to_file(self):
        '''Test method save_to_file which writes the JSON 
        string representation of list_objs to a file'''
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(print(sorted(file.read())), '[{"height": 7, "id": 1,
            "width": 10, "x": 2, "y": 8}, {"height": 4, "id": 2,
            "width": 2, "x": 0, "y": 0}]')

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(print(sorted(file.read())), '[]')

                             
    def test_from_json_string(self):
        '''Test methon - from_json_string which returns the list 
        of the JSON string representation json_string'''
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = sorted(Rectangle.from_json_string(json_list_input))
        self.assertEqual(print("[{}] {}".format(type(list_input), list_input)),
                         "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89},
                                           {'height': 7, 'width': 1, 'id': 7}]")
        self.assertEqual(print("[{}] {}".format(type(json_list_input),
                                                json_list_input)),
                         '[<class 'str'>] [{"height": 4, "width": 10, "id": 89},
                                          {"height": 7, "width": 1, "id": 7}]')
        self.assertEqual(print("[{}] {}".format(type(list_output), list_output)),
                         "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89},
                                           {'height': 7, 'width': 1, 'id': 7}]")
                             
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(print(list_output), '[]')
