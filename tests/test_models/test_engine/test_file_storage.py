#!/usr/bin/python3
"""
Test for the file storage module
"""


import json
import os
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine import file_storage
import models
import sys


class EngineStorageDocTest(unittest.TestCase):
    """
    Test the docs of the file engine
    """

    def test_doc(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(file_storage.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(FileStorage.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.__init__.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.new.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.save.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(FileStorage.reload.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/engine/file_storage.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )


class TestEngineFileStorage(unittest.TestCase):
    """
    Check the File Storage Class
    """

    def setUp(self):
        """
        Set up all the test
        """
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """
        Close all the test
        """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_createNewInstance(self):
        """
        Check the creation of news instances, check if there are well
        implemented
        into the storage dict
        """
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newPlace = Place()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        for className in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(className, models.storage.all().keys())

    def test_checkSave(self):
        """
        Check the creation of news instances, check if there are well
        implemented
        into the json file
        """
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newPlace = Place()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        models.storage.save()
        with open("file.json", 'r') as f:
            buf = json.load(f)
        for className in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(className, buf.keys())

    def test_checkRelaod(self):
        """
        Check the creation of news instances, check if there are well
        implemented
        with the realod method
        """
        newBaseModel = BaseModel()
        newAmenity = Amenity()
        newPlace = Place()
        newCity = City()
        newReview = Review()
        newState = State()
        newUser = User()
        models.storage.save()
        FileStorage._FileStorage__objects = {}
        models.storage.reload()
        for className in ["BaseModel." + newBaseModel.id,
                          "Amenity." + newAmenity.id,
                          "Place." + newPlace.id,
                          "City." + newCity.id,
                          "Review." + newReview.id,
                          "State." + newState.id,
                          "User." + newUser.id]:
            self.assertIn(className, models.storage.all().keys())

    def test_checkArgu(self):
        """
        Check all method with arguments
        """
        with self.assertRaises(AttributeError):
            models.storage.new("Coucou")
        with self.assertRaises(TypeError):
            models.storage.save("Coucou")
        with self.assertRaises(TypeError):
            models.storage.all("Coucou")
        with self.assertRaises(TypeError):
            models.storage.reload("Coucou")
        sys.stderr.write("FAIL")
