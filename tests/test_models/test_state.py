#!/usr/bin/python3
"""
Unitest for the State Class
"""

import unittest
import pycodestyle
from models import state
from models.state import State
import models


class TestState(unittest.TestCase):
    """
    Test all the State Class case
    """

    def test_doc(self):
        """
        Check all the doc of the City Class
        """
        module = len(state.__doc__)
        self.assertGreater(module, 0)

        module_class = len(State.__doc__)
        self.assertGreater(module_class, 0)

    def test_PEP8(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/state.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def setUp(self):
        """setUp all instance we need"""
        self.myState = State()

    def tearDown(self):
        """tearDown delete all instance"""
        del self.myState

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.myState, models.storage.all().values())

    def test_attribute_exist(self):
        """
        Check if attribute are here
        """
        self.assertTrue("name" in dir(self.myState))

    def test_attribute(self):
        """
        Check if there are in good type
        """
        self.assertTrue(type(self.myState.name) is str)

    def test_strRepr(self):
        """
        Check the string representation of the State class
        """
        self.myState.name = "Isère"
        strRep = self.myState.__str__()
        self.assertIn(f"[State] ({self.myState.id})", strRep)
        self.assertIn(f"'id': '{self.myState.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.myState.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.myState.updated_at)}", strRep)
        self.assertIn(
            f"'name': '{self.myState.name}'", strRep)
