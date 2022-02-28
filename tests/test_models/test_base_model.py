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

    def createModel(self):
        """
        Create to instance of the Base Model
        """
        myModelOne = BaseModel()
        time.sleep(0, 5)
        myModelTwo = BaseModel()

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

    def test_idStr(self):
        self.assertEqual(type(myModel.id), str)

    def test_uniqueId(self):
        self.assertNotEqual(myModelOne.id, myModelTwo.id)

    def test_DateTimeCreated(self):
        self.assertEqual(myModel.created_at, myModel.update_at)
        self.assertNotEqual(myModelOne.created_at, myModelTwo.created_at)
        self.assertNotEqual(myModelOne.update_at, myModelTwo.updated_at)
        myModelTwo.save()
        self.assertNotEqual(myModelTwo.created_at, myModelTwo.updated_at)

    def test_strRepr(self):
        strRep = myModelOne.__str__
        self.assertIn(f"[BaseModel] ({myModelOne.id}): ", strRep)
        self.assertIn(f"'id': '{myModelOne.id}'", strRep)
        """
        ...
        """

    def test_ToDictContainsAddedAttributes(self):
        myModelOne.name = "Holberton"
        myModelOne.my_number = 98
        self.assertIn("name", myModelOne.to_dict())
        self.assertIn("my_number", myModelOne.to_dict())

class TestBaseConstructor(unittest.TestCase):
    '''
    The class for test the constructor of base models
    '''

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
