#!/usr/bin/python3
'''
Test suite for the rectangle model
'''
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_base(self):
        """Tries to check if Rectangle inherits from Base"""
        r1 = Rectangle(2, 2)
        self.assertTrue(isinstance(r1, Base))

    def test_base_id_does_not_reset(self):
        """Checks if Rectangle class has access to Base class's id
           attribute and Base is aware"""
        self.assertEqual(Base(id=2).id, 2)
    
    def test_get_id_from_base(self):
        """Checks if Rectangle class has access to Base class's id
           attribute"""
        r1 = Rectangle(2, 2, id=1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(Rectangle(4, 3, id=3).id, 3)

    def test_setter_methods_validation(self):
        """Test validity(setter validations) of setter methods"""
        width = 2
        height = 4
        
        """Validity for width"""
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle('two', height)
            self.assertEqual('width must be an integer', e)
        with self.assertRaises(TypeError) as e:
            r2 = Rectangle('two', 'four')
            self.assertEqual('width must be an integer', e)
        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(-1, 3)
            self.assertEqual('width must be > 0', e)
        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(-1, -3)
            self.assertEqual('width must be > 0', e)
        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(0, 3)
            self.assertEqual('width must be > 0', e)
        with self.assertRaises(ValueError) as e:
            r2 = Rectangle(0, 0)
            self.assertEqual('width must be > 0', e)

        """Validity for height"""
        with self.assertRaises(TypeError) as e:
            r3 = Rectangle(width, 'four')
            self.assertEqual('height must be an integer', e)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, -3)
            self.assertEqual('height must be > 0', e)
        with self.assertRaises(ValueError) as e:
            r3 = Rectangle(1, 0)
            self.assertEqual('height must be > 0', e)

        '''Validity for x'''
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(width, height, 'two', 4)
            self.assertEqual('x must be an integer', e)
        with self.assertRaises(TypeError) as e:
            r4 = Rectangle(width, height, 'two', 'four')
            self.assertEqual('x must be an integer', e)
        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(width, height, -2, 4)
            self.assertEqual('x must be >= 0', e)
        with self.assertRaises(ValueError) as e:
            r4 = Rectangle(1, 3, -2, -4)
            self.assertEqual('x must be >= 0', e)
        
        '''Validity for y'''
        with self.assertRaises(TypeError) as e:
            r5 = Rectangle(width, height, 3, 'four')
            self.assertEqual('y must be an integer', e)
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 3, 2, -4)
            self.assertEqual('y must be >= 0', e)

    def test_area_method(self):
        """Test the area method meant to return the area
           of a Rectangle instance"""
        r2 = Rectangle(2, 2, 0, 0, 4)
        self.assertEqual(r2.area(), 4)

    def test_display_method(self):
        """Test the public display method meant to print to
           stdout the Rectangle instance with the character #"""
        r3 = Rectangle(2, 2, 0, 0, 5)
        self.assertEqual(r3.display(), f'##\n##')
        
        """Test if x and y coordinate works"""
        r4 = Rectangle(2, 3, 2, 2, 6)
        self.assertEqual(r4.display(), f'\n\n  ##\n  ##\n  ##')
        r5 = Rectangle(3, 2, 1, 0, 7)
        self.assertEqual(r5.display(), f' ###\n ###')

    def test_str_return(self):
        """Test the return value of magic __str__()"""
        r6 = Rectangle(2, 2, 0, 0, 8)
        self.assertEqual(r6.__str__(), '[Rectangle] (8) 0/0 - 2/2')

    def test_update_method_0(self):
        """Test the update method as update(self, *args)"""
        r7 = Rectangle(10, 10, 10, 10, 9)
        self.assertEqual(r7.__str__(), '[Rectangle] (9) 10/10 - 10/10')
        r7.update(89)
        self.assertEqual(r7.__str__(), '[Rectangle] (89) 10/10 - 10/10')
        r7.update(89, 2)
        self.assertEqual(r7.__str__(), '[Rectangle] (89) 10/10 - 2/10')
        r7.update(89, 2, 3)
        self.assertEqual(r7.__str__(), '[Rectangle] (89) 10/10 - 2/3')
        r7.update(89, 2, 3, 4)
        self.assertEqual(r7.__str__(), '[Rectangle] (89) 4/10 - 2/3')
        r7.update(89, 2, 3, 4, 5)
        self.assertEqual(r7.__str__(), '[Rectangle] (89) 4/5 - 2/3')

    def test_update_method_1(self):
        """Test the update method as update(self, *args, **kwargs)"""
        r8 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r8.__str__(), '[Rectangle] (1) 10/10 - 10/10')
        r8.update(height=1)
        self.assertEqual(r8.__str__(), '[Rectangle] (1) 10/10 - 10/1')
        r8.update(width=1, x=2)
        self.assertEqual(r8.__str__(), '[Rectangle] (1) 2/10 - 1/1')
        r8.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r8.__str__(), '[Rectangle] (89) 3/1 - 2/1')
        r8.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r8.__str__(), '[Rectangle] (89) 1/3 - 4/2')

    def test_to_dictionary(self):
        """test the method to_dictionary meant to return 
        the dictionary representation of a Rectangle"""
        r9 = Rectangle(10, 2, 1, 9, 1)
        self.assertEqual(r9.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        r9_dictionary = r9.to_dictionary()
        self.assertDictEqual(r9_dictionary, {'height': 2, 'id': 1, 'x': 1, 'width': 10, 'y': 9})
        self.assertEqual(type(r9_dictionary), dict)
        r10 = Rectangle(1, 1, id=2)
        self.assertEqual(r10.__str__(), '[Rectangle] (2) 0/0 - 1/1')
        r10.update(**r9_dictionary)
        self.assertEqual(r10.__str__(), '[Rectangle] (1) 1/9 - 10/2')
        self.assertFalse(r9 == r10)
