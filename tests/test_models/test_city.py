#!/usr/bin/python3
""" Testing city class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ testing City class"""

    def __init__(self, *args, **kwargs):
        """ a constructor method"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ testing state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ testing name"""
        new = self.value()
        self.assertEqual(type(new.name), str)
