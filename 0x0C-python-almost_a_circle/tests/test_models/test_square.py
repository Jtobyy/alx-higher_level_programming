#!/usr/bin/python3
'''
Test suite for the rectangle model
'''
import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    s1 = square(2)
    def test_super(self):
        '''Tries to check if Square inherits from Rectangle'''
        self.assertIsInstance(s1, (Square, Rectangle))

     def test_str_return(self):
        '''Test the return value of magic __str__()'''
        self.assertEqual(print(s1), '[Square] (1) 0/0 - 2')

    def test_get_private_attrs(self):
        '''Checks if attributes meant to be private are private'''
        with self.assertRaises('AttributeError'):
            s1.__size
        with self.assertRaises('AttributeError'):
            s1.__x
        with self.assertRaises('AttributeError'):
            s1.__y
        with self.assertRaises('AttributeError'):
            s1.size
        with self.assertRaises('AttributeError'):
            s1.x
        with self.assertRaises('AttributeError'):
            s1.y

    def test_get_id_from_base(self):
        '''Checks if Square class has access to Base class's id
           attribute '''
        self.assertEqual(s1.id, 1)
        self.assertEqual(Square().id, 2)

    def test_base_id_does_not_reset(self):
        '''Checks if Square class has access to Base class's id
           attribute and Base is aware'''
        self.assertEqual(Base().id, 3)
        self.assertEqual(Rectangle().id, 4)

    def test_get_attrs_with_getters(self):
        '''Checks if getters are implemented for private attributes'''
        self.assertEqual(s1.get_size(), 2)
        self.assertEqual(s1.get_x(), 0)
        self.assertEqual(s1.get_y(), 0)

    def test_setters_work_for_attrs(self):
        '''Checks if setters are implemented for private attributes'''
        s1.set_size(4)
        self.assertEqual(s1.get_size(), 4)
        self.assertEqual(s1.get_width(), 4)
        self.assertEqual(s1.get_height(), 4)
        s1.set_x(2)
        self.assertEqual(s1.get_x(), 2)
        s1.set_y(2)
        self.assertEqual(s1.get_y(), 2)

    def test_setter_methods_validation(self):
        '''Test validity(setter validations) of setter methods'''
        size = 4
        
        '''Validity for size(width used)'''
        with self.assertRaises('TypeError') as e:
            s2 = Square('four')
        self.assertEqual('width must be an integer', e)
        with self.assertRaises('ValueError') as e:
            s2 = Square(-1)
        self.assertEqual('width must be > 0', e)
        with self.assertRaises('ValueError') as e:
            s2 = Square(0)
        self.assertEqual('width must be > 0', e)

        '''Validity for x'''
        with self.assertRaises('TypeError') as e:
            s4 = Square(size, 'two', 4)
        self.assertEqual('x must be an integer', e)
        with self.assertRaises('TypeError') as e:
            s4 = Square(size, 'two', 'four')
        self.assertEqual('x must be an integer', e)
        with self.assertRaises('ValueError') as e:
            s4 = Square(size, -2, 4)
        self.assertEqual('x must be >= 0', e)
        with self.assertRaises('ValueError') as e:
            s4 = Square(size, -2, -4)
        self.assertEqual('x must be >= 0', e)
        
        '''Validity for y'''
        with self.assertRaises('TypeError') as e:
            s5 = Square(size, 3, 'four')
        self.assertEqual('y must be an integer', e)
        with self.assertRaises('ValueError'):
            s5 = Square(size, 2, -4)
        self.assertEqual('y must be >= 0', e)

    def test_square_update_method(self):
        '''Test the update method as update(self, *args)'''
        s6 = Square(5)
        self.assertEqual(print(s6), '[Square] (1) 0/0 - 5')
        s6.update(10)
        self.assertEqual(print(s6), '[Square] (10) 0/0 - 5')
        s6.update(1, 2)
        self.assertEqual(print(s6), '[Square] (1) 0/0 - 2')
        s6.update(1, 2, 3)
        self.assertEqual(print(s6), '[Square] (1) 3/10 - 2')
        s6.update(1, 2, 3, 4)
        self.assertEqual(print(s6), '[Square] (1) 3/4 - 2')
        s6.update(x=12)
        self.assertEqual(print(s6), '[Square] (1) 12/4 - 2')
        s6.update(size=7, y=1)
        self.assertEqual(print(s6), '[Square] (1) 12/1 - 7')
        s6.update(size=7, id=89, y=1)
        self.assertEqual(print(s6), '[Square] (89) 12/1 - 7')

    def test_to_dictionary(self):
        '''test the method to_dictionary meant to return 
        the dictionary representation of a Square'''
        s7 = Square(10, 2, 1, id=1)
        self.assertEqual(print(s7), '[Square] (1) 2/1 - 10')
        s7_dictionary = s7.to_dictionary()
        self.assertEqual(print(sorted(s7_dictionary)), '''{'id': 1, 'size': 10,
        'x': 2, 'y': 1'''}
        self.assertEqual(print(type(s7_dictionary)), "<class 'dict'>")
        s8 = Square(1, 1, id=2)
        self.assertEqual(print(s8), '[Square] (2) 1/0 - 1')
        s8.update(**s7_dictionary)
        self.assertEqual(print(s8), '[Square] (1) 2/1 - 10')
        self.assertFalse(s7 == s8)

        
