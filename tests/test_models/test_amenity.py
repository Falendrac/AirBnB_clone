#!/usr/bin/python3
"""
Unitest for the base model class
"""


import unittest
import pycodestyle
import time
from datetime import datetime
from models import amenity
from models.amenity import Amenity
import os


class TestAmenity(unittest.TestCase):
    """
    Test all the feature of the task 3 on the Base Model Class
    """

    def test_doc(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(amenity.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(Amenity.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(Amenity.to_dict.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base_model.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def setUp(self):
        """setUp all instance we need"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.my_model1 = Amenity()
        self.my_model2 = Amenity()
        self.my_model1.name = "My_First_Model"
        self.my_model1.my_number = 89
        self.my_model_json = self.my_model1.to_dict()

    def tearDown(self):
        """tearDown delete all instance"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        del self.my_model1
        del self.my_model2
        del self.my_model_json

    def test_idStr(self):
        """test if id is a string"""
        self.assertEqual(type(self.my_model1.id), str)

    def test_uniqueId(self):
        """test if id is unique"""
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_DateTimeCreated(self):
        """test if date is created"""
        self.assertEqual(self.my_model1.created_at, self.my_model1.updated_at)
        self.assertNotEqual(self.my_model1.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model1.updated_at,
                            self.my_model2.updated_at)
        self.my_model2.save()
        self.assertNotEqual(self.my_model2.created_at,
                            self.my_model2.updated_at)

    def test_strRepr(self):
        """test if is good repr of class"""
        strRep = self.my_model1.__str__()
        self.assertIn(f"[Amenity] ({self.my_model1.id})", strRep)
        self.assertIn(f"'id': '{self.my_model1.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.my_model1.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.my_model1.updated_at)}", strRep)

    def test_ToDictContainsAddedAttributes(self):
        """test dict"""
        self.assertIn("name", self.my_model_json)
        self.assertIn("my_number", self.my_model_json)

    def test_attribute_exist(self):
        """test attribute"""
        self.assertTrue("name" in dir(self.my_model2))

    def test_attribute_type(self):
        """test attribute type"""
        self.assertTrue(type(self.my_model2.name) is str)

    def test_attribute_empty(self):
        """test if attribute is empty"""
        self.assertTrue(self.my_model2.name == "")

    def test_attribute_change(self):
        """test attribute change"""
        self.my_model2.name = 48

        self.assertTrue(type(self.my_model2.name) is not str)
        self.assertTrue(self.my_model2.name == 48)

    def test_serialization(self):
        """test serialization"""
        self.assertEqual(
            str(self.my_model1),
            f"[Amenity] ({self.my_model1.id}) {self.my_model1.__dict__}"
        )
        dictJson = self.my_model1.__dict__.copy()
        dictJson["__class__"] = self.my_model1.__class__.__name__
        dictJson["created_at"] = dictJson["created_at"].isoformat()
        dictJson["updated_at"] = dictJson["updated_at"].isoformat()
        self.assertEqual(self.my_model1.to_dict(), dictJson)


class TestAmenityConstructor(unittest.TestCase):
    """
    The class for test the constructor of Amenity
    """

    def setUp(self):
        """setUp all instance we need"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.my_model = Amenity()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.my_new_model = Amenity(**self.my_model_json)
        self.my_new_model_other = Amenity(**self.my_model_json)

        self.my_new_model_other.magic_number = 42

        self.other_model = Amenity(54, "lol", "shakazulu", 34643)

    def tearDown(self):
        """tearDown delete all instance"""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        del self.my_model
        del self.my_model_json
        del self.my_new_model
        del self.my_new_model_other
        del self.other_model

    def test_base_equal(self):
        """test all equal cases"""
        self.assertEqual(self.my_new_model.id, self.my_model.id)
        self.assertEqual(self.my_new_model_other.id, self.my_model.id)
        self.assertEqual(self.my_new_model.__str__(), self.my_model.__str__())
        self.assertEqual(type(self.my_new_model.created_at), datetime)
        self.assertEqual(type(self.other_model.created_at), datetime)

    def test_base_notequal(self):
        """test all not equal cases"""
        self.assertNotEqual(self.my_new_model_other, self.my_new_model)
        self.assertNotEqual(self.my_new_model.id, self.other_model.id)
        self.assertNotEqual(self.my_new_model.__str__(),
                            self.other_model.__str__())

    def test_base_false(self):
        """test all false cases"""
        self.assertFalse(self.my_model is self.my_new_model)
        self.assertFalse(self.other_model is self.my_new_model)
