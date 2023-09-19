#!/usr/bin/python3
""" testing Amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """ testing amenity class """

    def __init__(self, *args, **kwargs):
        """ a constructor method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test name2"""
        new = self.value()
        self.assertEqual(type(new.name), str)
