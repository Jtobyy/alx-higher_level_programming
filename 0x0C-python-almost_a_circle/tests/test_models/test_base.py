#!/usr/bin/python3
"""
Test suite for base
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_Base(self):
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
        with self.assertRaises(AttributeError):
            b1 = Base()
            b1.nb_objects
        with self.assertRaises(AttributeError):
            b6 = Base()
            b6.__nb_objects
            
    def test_to_json_string(self):
        b7 = Base(8)
        self.assertEqual(b7.to_json_string(None), '[]')
        self.assertEqual(b7.to_json_string(None), '[]')
        self.assertEqual(b7.to_json_string(None), '[]')

        r1 = Rectangle(10, 7, 2, 8, id=1)
        dictionary = r1.to_dictionary()

        json_dictionary = r1.to_json_string([dictionary])
        self.assertEqual(dictionary, {"width": 10, "height": 7, "x": 2, "y": 8, "id": 1})
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(json_dictionary, '[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 1}]')
        self.assertEqual(type(json_dictionary), str)
      
    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8, id=1)
        r2 = Rectangle(2, 4, id=2)
        Rectangle.save_to_file([r1, r2])
        
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '''[{"width": 10, "height": 7, "x": 2, "y": 8, "id": 1}, {"width": 2, "height": 4, "x": 0, "y": 0, "id": 2}]''')

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_from_json_string(self):
        list_input = [
                    {'id': 89, 'width': 10, 'height': 4},
                    {'id': 7, 'width': 1, 'height': 7}
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_input), list)
        self.assertEqual(list_input, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
                                      
        self.assertEqual(type(json_list_input), str)
        self.assertEqual(json_list_input, '[{"id": 89, "width": 10, "height": 4}, {"id": 7, "width": 1, "height": 7}]')

        self.assertEqual(type(list_output), list)
        self.assertEqual(list_output, [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}])
                
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, '[]')
