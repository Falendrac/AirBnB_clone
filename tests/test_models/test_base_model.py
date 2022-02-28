#!/usr/bin/python3
import unittest
import doctest
import time

BaseModel = __import__("base_model.py").max_integer

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
