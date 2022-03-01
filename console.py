#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
import models

classes = ("BaseModel")


class HBNBCommand(cmd.Cmd):
    """
    The console class
    """
    prompt = '(hbnb) '

    def emptyline(self):
        print(end="")

    def do_EOF(self, line):
        """
        Manage the EOF
        """
        return True

    def do_quit(self, line):
        """
        Quit the program
        """
        return True

    def do_create(self, className):
        """
        Create a new instance of the given class
        Usage: create <NameClass>
        Exceptions:
            If the name class do not exist
            If the name class isn't given
        """
        if not className:
            print("** class name missing **")
        try:
            newClass = eval(className)()
            print(newClass.id)
            newClass.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        """
        if not line:
            print("** class name missing ** ")
            return False
        data = line.split(" ")
        if data[0] not in classes:
            print("** class doesn't exist **")
            return False
        if len(data) == 1:
            print("** instance id missing **")
            return False

    def help_EOF(self):
        """
        Help section of EOF
        """
        print('\n'.join(
            ['Manage the EOF, exit the console and save all the created instance']))

    def help_quit(self):
        """
        Help section of quit
        """
        print('\n'.join(
            ['Quit function\nUsage quit\nExit the console and save all the created instance']))

    def help_create(self):
        """
        Help section of create
        """
        print('\n'.join(
            ['Create function\nUsage create <ClassName>\nCreate a new instance of the given class, print its id']))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
