#!/usr/bin/python3
"""
Create the Base Model class
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The Base Model of the AirBnB
    """

    def __init__(self, *args, **kwargs):
        """
        Init the Base Model class
        """
        if len(kwargs) == 0:
            timming = datetime.now()
            self.id = str(uuid.uuid4())
            self.created_at = timming
            self.updated_at = timming
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key != 'created_at' and key != 'updated_at':
                        setattr(self, key, val)
                    else:
                        setattr(self, key, datetime.fromisoformat(val))

    def __str__(self):
        """
        Create a representation of the str
        """
        str = f"[BaseModel] ({self.id}) {self.__dict__}"
        return str

    def save(self):
        """
        Save the model base to the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Create a dict representation of the class
        """
        dictJson = self.__dict__.copy()
        dictJson["__class__"] = self.__class__.__name__
        dictJson["created_at"] = dictJson["created_at"].isoformat()
        dictJson["updated_at"] = dictJson["updated_at"].isoformat()
        return dictJson
