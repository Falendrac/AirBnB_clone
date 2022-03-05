#!/usr/bin/python3
"""
Unitest for the City Class
"""

import unittest
import pycodestyle
from models import city
from models.city import City
import models


class TestCity(unittest.TestCase):
    """
    Test all the city class case
    """

    def test_doc(self):
        """
        Check all the doc of the City Class
        """
        module = len(city.__doc__)
        self.assertGreater(module, 0)

        module_class = len(City.__doc__)
        self.assertGreater(module_class, 0)

    def test_PEP8(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/city.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def setUp(self):
        """setUp all instance we need"""
        self.myCity = City()

    def tearDown(self):
        """tearDown delete all instance"""
        del self.myCity

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.myCity, models.storage.all().values())

    def test_attribute_exist(self):
        """
        Check if attribute are here
        """
        self.assertTrue("state_id" in dir(self.myCity))
        self.assertTrue("name" in dir(self.myCity))

    def test_attribute(self):
        """
        Check if there are in good type
        """
        self.assertTrue(type(self.myCity.state_id) is str)
        self.assertTrue(type(self.myCity.name) is str)

    def test_strRepr(self):
        """
        Check the string representation of the City class
        """
        self.myCity.state_id = "38"
        self.myCity.name = "Grenoble"
        strRep = self.myCity.__str__()
        self.assertIn(f"[City] ({self.myCity.id})", strRep)
        self.assertIn(f"'id': '{self.myCity.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.myCity.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.myCity.updated_at)}", strRep)
        self.assertIn(
            f"'state_id': '{self.myCity.state_id}'", strRep)
        self.assertIn(
            f"'name': '{self.myCity.name}'", strRep)
