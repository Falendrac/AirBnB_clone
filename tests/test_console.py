#!/usr/bin/python3
"""
Test for the console.py
"""

import os
import unittest
import models
import json
import cmd
from io import StringIO
from console import HBNBCommand
import console
import pycodestyle
from unittest.mock import patch
from models.engine.file_storage import FileStorage


class TestBasicCaseAndDoc(unittest.TestCase):
    """
    Test the whole docs, and basic input
    """

    def test_doc(self):
        """
        Check all the doc of the Amenity Class
        """
        # module documentation
        module = len(console.__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(HBNBCommand.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_create.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_show.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_quit.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_EOF.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_count.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_destroy.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.do_update.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.emptyline.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.default.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_all.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_create.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_EOF.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_destroy.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_quit.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_show.__doc__)
        self.assertGreater(module_class, 0)

        module_class = len(HBNBCommand.help_update.__doc__)
        self.assertGreater(module_class, 0)

    def test_pycodeStyle(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_prompt(self):
        """
        Test the prompt
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """
        Check the case of empty line
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual("", f.getvalue().strip())

    def test_UnknowCommand(self):
        """
        Test an unknow command
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("fdfdf")
            self.assertEqual("*** Unknown syntax: fdfdf", f.getvalue().strip())


class TestHelpFunction(unittest.TestCase):
    """
    Check all the help functions
    """

    def test_helpCreate(self):
        """
        Test the help function of create
        """
        helpStr = 'Create function\n\
Usage create <ClassName>\n\
Create a new instance of the given class, print its id\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpShow(self):
        """
        Test the help function of show
        """
        helpStr = 'Show a instance by using the Nameclass and its ID\n\
Usage: show <ClassName> <Id>\n\
Show the __str__ representation of the class\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpDestroy(self):
        """
        Test the help function of destroy
        """
        helpStr = 'Destroy a instance by using the Nameclass and its ID\n\
Usage: destroy <ClassName> <Id>\n\
Destroy the instance, and save it into the Json file\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpAll(self):
        """
        Test the help function of all
        """
        helpStr = "Display all instance of a class\n\
Usage: all <className>\n"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpUpdate(self):
        """
        Test the help function of update
        """
        helpStr = 'Update an attribute of an instance.\n\
Usage: update <class name> <id> <attribute name> "<attribute value>"\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpEOF(self):
        """
        Test the help function of EOF
        """
        helpStr = 'Manage the EOF, exit the console and\
save all the created instance\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertGreater(helpStr, f.getvalue().strip())

    def test_helpQuit(self):
        """
        Test the help function of quit
        """
        helpStr = 'Quit function\n\
Usage quit\n\
Exit the console and save all the created instance\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertGreater(helpStr, f.getvalue().strip())


class TestFunctions(unittest.TestCase):
    """
    Test all the functions
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

    def test_create(self):
        """
        Check the create functions
        Check first all the edges cases, then the creation of
        instances
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create LesTestCesSuicidaire")
            self.assertEqual(output, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
            className = "BaseModel." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
            className = "User." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
            className = "Amenity." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
            className = "City." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
            className = "Place." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
            className = "Review." + id
            self.assertIn(className, models.storage.all().keys())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
            className = "State." + id
            self.assertIn(className, models.storage.all().keys())

    def test_show(self):
        """
        Check the create functions
        Check first all the edges cases, then the creation of
        instances
        """
        output = "** class name missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(output, f.getvalue().strip())
        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show NotGoodClasses")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel NotGoodID")
            self.assertEqual(output, f.getvalue().strip())

        output = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("NotGoodClasses.show()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** instance id missing **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
            self.assertEqual(output, f.getvalue().strip())
        output = "** no instance found **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(NotGoodID)")
            self.assertEqual(output, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel " + id)
            className = f"[BaseModel] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({id})")
            className = f"[BaseModel] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User " + id)
            className = f"[User] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({id})")
            className = f"[User] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Amenity " + id)
            className = f"[Amenity] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({id})")
            className = f"[Amenity] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show City " + id)
            className = f"[City] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({id})")
            className = f"[City] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place " + id)
            className = f"[Place] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({id})")
            className = f"[Place] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Review " + id)
            className = f"[Review] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({id})")
            className = f"[Review] ({id})"
            self.assertIn(className, f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show State " + id)
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({id})")
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.      show(     {id}     )")
            className = f"[State] ({id})"
            self.assertIn(className, f.getvalue().strip())