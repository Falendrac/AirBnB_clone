#!/usr/bin/python3
"""
Creation of the console of the web application
"""

import cmd
from models.base_model import BaseModel
import models

classes = ("BaseModel", "User", "State", "City", "Amenity", "Place", "Review")


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
        Show a instance by his ID and class name
        Usage: show <ClassName> <Id>
        Exceptions:
            If the name class is missing
            If the class do not exist
            Id is missing
            If the Id do not exist
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
        classNameId = f"{data[0]}.{data[1]}"
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        print(models.storage.all()[classNameId])

    def do_destroy(self, line):
        """
        Destroy a instance by his ID and class name
        Usage: destroy <ClassName> <Id>
        Exceptions:
            If the name class is missing
            If the class do not exist
            Id is missing
            If the Id do not exist
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
        classNameId = f"{data[0]}.{data[1]}"
        if classNameId not in models.storage.all():
            print("** no instance found **")
            return False
        del models.storage.all()[classNameId]
        models.storage.save()

    def do_all(self, line):
        instanceListStr = []
        if not line:
            for instance in models.storage.all().values():
                instanceListStr.append(instance.__str__())
        else:
            if line not in classes:
                print("** class doesn't exist **")
                return False
            for instance in models.storage.all().values():
                if instance.__class__.__name__ == line:
                    instanceListStr.append(instance.__str__())
        print(instanceListStr)

    def do_update(self, line):
        """
        Update an attribute of an instance.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
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
        strLine = f"{data[0]}.{data[1]}"
        if strLine not in models.storage.all():
            print("** no instance found **")
            return False
        if len(data) == 2:
            print("** attribute name missing **")
            return False
        if len(data) == 3:
            print("** value missing **")
            return False
        currentInstance = models.storage.all()[strLine]
        if data[2] != "id" or data[2] != "created_at" or data[2] != "updated_at":
            setattr(currentInstance, data[2], data[3])
        models.storage.save()

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

    def help_show(self):
        """
        Help section of show
        """
        print('\n'.join(
            ['Show a instance by using the Nameclass and its ID\nUsage: show <ClassName> <Id>\nShow the __str__ representation of the class']))

    def help_destroy(self):
        """
        Help section of destroy
        """
        print('\n'.join(
            ['Destroy a instance by using the Nameclass and its ID\nUsage: destroy <ClassName> <Id>\nDestroy the instance, and save it into the Json file']))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
