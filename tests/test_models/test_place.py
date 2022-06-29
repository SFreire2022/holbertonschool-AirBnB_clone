#!/usr/bin/python3
""" Unittest for all the methods of the class Place
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.place import Place


class TestAmenityModule(unittest.TestCase):
    """ A class to test Place Module """
    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/place.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)
