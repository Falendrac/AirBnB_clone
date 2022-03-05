#!/usr/bin/python3
"""
Unitest for the Review Class
"""

import unittest
import pycodestyle
from models import review
from models.review import Review
import models


class TestReview(unittest.TestCase):
    """
    Test all the Review Class case
    """

    def test_doc(self):
        """
        Check all the doc of the City Class
        """
        module = len(review.__doc__)
        self.assertGreater(module, 0)

        module_class = len(Review.__doc__)
        self.assertGreater(module_class, 0)

    def test_PEP8(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/review.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def setUp(self):
        """setUp all instance we need"""
        self.myReview = Review()

    def tearDown(self):
        """tearDown delete all instance"""
        del self.myReview

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.myReview, models.storage.all().values())

    def test_attribute_exist(self):
        """
        Check if attribute are here
        """
        self.assertTrue("place_id" in dir(self.myReview))
        self.assertTrue("user_id" in dir(self.myReview))
        self.assertTrue("text" in dir(self.myReview))

    def test_attribute(self):
        """
        Check if there are in good type
        """
        self.assertTrue(type(self.myReview.place_id) is str)
        self.assertTrue(type(self.myReview.user_id) is str)
        self.assertTrue(type(self.myReview.text) is str)

    def test_strRepr(self):
        """
        Check the string representation of the Review class
        """
        self.myReview.place_id = "09934-22334-23332-445234"
        self.myReview.user_id = "23323-23423-234423-23423"
        self.myReview.text = "So fun this place"
        strRep = self.myReview.__str__()
        self.assertIn(f"[Review] ({self.myReview.id})", strRep)
        self.assertIn(f"'id': '{self.myReview.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.myReview.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.myReview.updated_at)}", strRep)
        self.assertIn(
            f"'place_id': '{self.myReview.place_id}'", strRep)
        self.assertIn(
            f"'user_id': '{self.myReview.user_id}'", strRep)
        self.assertIn(
            f"'text': '{self.myReview.text}'", strRep)
