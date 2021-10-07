#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 2, 4, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertAlmostEqual(max_integer([4, 2, 3, -1]), 4)
        self.assertAlmostEqual(max_integer([4, 2, 7, 3, -1]), 7)
        self.assertAlmostEqual(max_integer([-4, -2, -3, -1]), -1)
        self.assertAlmostEqual(max_integer([-1]), -1)
