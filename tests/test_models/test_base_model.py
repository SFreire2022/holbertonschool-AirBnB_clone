#!/usr/bin/python3
""" Unittest for all the methods of the class Base
Check pycodestyle "PEP8" for the complete module """
import unittest
import pycodestyle
from models.base_model import BaseModel


class TestBaseModule(unittest.TestCase):
    """ A class to test Base Module """

    self.base_model1 = BaseModel()
    self.base_model2 = BaseModel()

    def test_pycodestyle_pep8(self):
        """ Style code meets PEP8 """
        style = pycodestyle.StyleGuide(quit=True)
        check = style.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            'PEP8 style errors: %d' % check.total_errors)

    def test_uuid(self):
        """ Test uuid """
        self.assertTrue(hasattr(self.base_model1, "id"))
        self.assertNotEqual(self.base_model1.id, self.base_model2.id)
        self.assertEqual(type(self.base_model1.id), str)
        self.assertEqual(type(self.base_model2.id), str)
