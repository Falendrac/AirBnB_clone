#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User

"""
Create a file storage class, to store all our data
"""


class FileStorage:
    """
    Class of our data storage
    """

    def __init__(self):
        """"
        Init the class.
        Var:
            __file_path (str): The path of our json file that cointain data
            __objects (dict): Contains all of our instance, as <class name>.id
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        Return the dictionary of all our objects
        """
        return self.__objects

    def new(self, obj):
        """
        Save the new object given into the obj dict
        Args:
            obj (object): The object to push into the dict
                        as <obj class name>.id = obj
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
        Save the current value of __object into a json file
        """
        dict_json = {}
        for key in self.__objects.keys():
            dict_json[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w+", encoding="utf-8") as file:
            json.dump(dict_json, file)

    def reload(self):
        """
        Read the saved json file, and realod the content into the __object attribute
        """
        try:
            with open(self.__file_path, "r+") as file:
                dictJson = json.load(file)
                for key, value in dictJson.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except:
            pass
