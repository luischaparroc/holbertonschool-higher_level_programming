#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """ Test string id """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
