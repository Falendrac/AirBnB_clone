#!/usr/bin/python3
import unittest
import pycodestyle
import time
from datetime import datetime
from models import base_model
from models.base_model import BaseModel

"""
Unitest for the base model class
"""


class TestBaseModelTask3(unittest.TestCase):
    """
    Test all the feature of the task 3 on the Base Model Class
    """

    def test_doc(self):
        """
        Check all the doc of the BaseModel Class
        """
        # module documentation
        module = len(base_model.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(BaseModel.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.__str__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(BaseModel.to_dict.__doc__)
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
        self.my_model1 = BaseModel()
        self.my_model2 = BaseModel()
        self.my_model1.name = "My_First_Model"
        self.my_model1.my_number = 89
        self.my_model_json = self.my_model1.to_dict()

    def tearDown(self):
        """tearDown delete all instance"""
        del self.my_model1
        del self.my_model2
        del self.my_model_json

    def test_idStr(self):
        self.assertEqual(type(self.my_model1.id), str)

    def test_uniqueId(self):
        self.assertNotEqual(self.my_model1.id, self.my_model2.id)

    def test_DateTimeCreated(self):
        self.assertEqual(self.my_model1.created_at, self.my_model1.updated_at)
        self.assertNotEqual(self.my_model1.created_at, self.my_model2.created_at)
        self.assertNotEqual(self.my_model1.updated_at, self.my_model2.updated_at)
        self.my_model2.save()
        self.assertNotEqual(self.my_model2.created_at, self.my_model2.updated_at)

    def test_strRepr(self):
        strRep = self.my_model1.__str__()
        self.assertIn(f"[BaseModel] ({self.my_model1.id})", strRep)
        self.assertIn(f"'id': '{self.my_model1.id}'", strRep)
        self.assertIn(f"'created_at': {repr(self.my_model1.created_at)}", strRep)
        self.assertIn(f"'updated_at': {repr(self.my_model1.updated_at)}", strRep)

    def test_ToDictContainsAddedAttributes(self):
        self.assertIn("name", self.my_model_json)
        self.assertIn("my_number", self.my_model_json)


class TestBaseConstructor(unittest.TestCase):
    """
    The class for test the constructor of base models
    """

    def setUp(self):
        """setUp all instance we need"""
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.my_new_model = BaseModel(**self.my_model_json)
        self.my_new_model_other = BaseModel(**self.my_model_json)

        self.my_new_model_other.magic_number = 42

        self.other_model = BaseModel(54, "lol", "shakazulu", 34643)

    def tearDown(self):
        """tearDown delete all instance"""
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
        self.assertNotEqual(self.my_new_model.__str__(), self.other_model.__str__())

    def test_base_false(self):
        """test all false cases"""
        self.assertFalse(self.my_model is self.my_new_model)
        self.assertFalse(self.other_model is self.my_new_model)
