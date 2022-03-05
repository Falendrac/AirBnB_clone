#!/usr/bin/python3
import unittest
import pycodestyle
import time
from datetime import datetime
from models import user
from models.user import User
import os

"""
Unitest for the base model class
"""


class TestUser(unittest.TestCase):
    """
    Test all the feature of the task 3 on the Base Model Class
    """

    def test_doc(self):
        """
        Check all the doc of the User Class
        """
        # module documentation
        module = len(user.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(User.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(User.to_dict.__doc__)
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
        self.my_model1 = User()
        self.my_model2 = User()
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
        self.assertEqual(type(self.my_model1.id), str)

    def test_uniqueId(self):
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_DateTimeCreated(self):
        self.assertEqual(self.my_model1.created_at, self.my_model1.updated_at)
        self.assertNotEqual(self.my_model1.created_at,
                            self.my_model2.created_at)
        self.assertNotEqual(self.my_model1.updated_at,
                            self.my_model2.updated_at)
        self.my_model2.save()
        self.assertNotEqual(self.my_model2.created_at,
                            self.my_model2.updated_at)

    def test_strRepr(self):
        strRep = self.my_model1.__str__()
        self.assertIn(f"[User] ({self.my_model1.id})", strRep)
        self.assertIn(f"'id': '{self.my_model1.id}'", strRep)
        self.assertIn(
            f"'created_at': {repr(self.my_model1.created_at)}", strRep)
        self.assertIn(
            f"'updated_at': {repr(self.my_model1.updated_at)}", strRep)

    def test_ToDictContainsAddedAttributes(self):
        self.assertIn("name", self.my_model_json)
        self.assertIn("my_number", self.my_model_json)

    def test_attribute_exist(self):
        self.assertTrue("email" in dir(self.my_model1))
        self.assertTrue("password" in dir(self.my_model1))
        self.assertTrue("first_name" in dir(self.my_model1))
        self.assertTrue("last_name" in dir(self.my_model1))

    def test_attribute_type(self):
        self.assertTrue(type(self.my_model1.email) is str)
        self.assertTrue(type(self.my_model1.password) is str)
        self.assertTrue(type(self.my_model1.first_name) is str)
        self.assertTrue(type(self.my_model1.last_name) is str)

    def test_attribute_empty(self):
        self.assertTrue(self.my_model1.email == "")
        self.assertTrue(self.my_model1.password == "")
        self.assertTrue(self.my_model1.first_name == "")
        self.assertTrue(self.my_model1.last_name == "")

    def test_attribute_change(self):
        self.my_model1.first_name = 48

        self.assertTrue(type(self.my_model1.first_name) is not str)
        self.assertTrue(self.my_model1.first_name == 48)

    def test_serialization(self):
        self.assertEqual(
            str(self.my_model1), f"[User] ({self.my_model1.id}) {self.my_model1.__dict__}")
        dictJson = self.my_model1.__dict__.copy()
        dictJson["__class__"] = self.my_model1.__class__.__name__
        dictJson["created_at"] = dictJson["created_at"].isoformat()
        dictJson["updated_at"] = dictJson["updated_at"].isoformat()
        self.assertEqual(self.my_model1.to_dict(), dictJson)


class TestUserConstructor(unittest.TestCase):
    """
    The class for test the constructor of User
    """

    def setUp(self):
        """setUp all instance we need"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.my_model = User()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.my_new_model = User(**self.my_model_json)
        self.my_new_model_other = User(**self.my_model_json)

        self.my_new_model_other.magic_number = 42

        self.other_model = User(54, "lol", "shakazulu", 34643)

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
