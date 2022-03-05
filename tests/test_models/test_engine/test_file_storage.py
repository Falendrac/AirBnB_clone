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

    path = "models/engine/file_storage.py"  # models/FileStorage.py
    file = os.path.splitext(path)[0].replace("/", ".")  # file to test

    def setUp(self):
        try:
            shutil.copyfile("file.json", "tmp_file.json")
            os.remove("file.json")
            open("file.json", "w").close()
        except Exception:
            pass

    def tearDown(self):
        try:
            shutil.copyfile("tmp_file.json", "file.json")
            os.remove("tmp_file.json")
        except Exception:
            pass

    def test_attributes_assignement(self):
        self.assertIn("_FileStorage__objects", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertIn("_FileStorage__file_path", FileStorage.__dict__)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)

    def test_all(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        models.storage._FileStorage__objects = {"Hello": "olleH"}
        self.assertTrue(models.storage.all())

    # def test_save(self):
    #     models.storage._FileStorage__objects = ""
    #     models.storage.save()
    #     with open("file.json", "r") as f:
    #         exception = f.read()
    #     self.assertTrue(exception)

    def test_reload(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        with open("file.json", "w") as f:
            f.write(json.dumps({
                "BaseModel.70549f31-bff4-4a34-bd10-b8eaaeb3bb6b":
                {"id": "70549f31-bff4-4a34-bd10-b8eaaeb3bb6b", "created_at":
                 "2022-03-01T20:27:24.506780", "updated_at":
                 "2022-03-01T20:27:24.506790", "__class__":
                 "BaseModel"}}))
        models.storage.reload()
        self.assertTrue(models.storage.all())

    def test_new(self):
        models.storage._FileStorage__objects = {}
        models.storage.new(User())
        models.storage.save()
        self.assertTrue(models.storage._FileStorage__objects)

    def test_save_new(self):
        models.storage._FileStorage__objects = {}
        self.assertFalse(models.storage.all())
        models.storage.new(User())
        models.storage.save()
        models.storage.reload()
        self.assertEqual(models.storage.all(), models.storage.__dict__[
                         '_FileStorage__objects'])
