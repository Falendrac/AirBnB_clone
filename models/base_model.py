#!/usr/bin/python3
"""
Create the Base Model class
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    The Base Model of the AirBnB
    """

    def __init__(self):
        """
        Init the Base Model class
        """
        timming = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = timming
        self.updated_at = timming

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

    def to_dict(self):
        """
        Create a dict representation of the class
        """
        dictJson = self.__dict__.copy()
        dictJson["__class__"] = self.__class__.__name__
        dictJson["created_at"] = datetime.isoformat(
            datetime.strptime(str(self.created_at), "%Y-%m-%d %H:%M:%S.%f")
        )
        dictJson["updated_at"] = datetime.isoformat(
            datetime.strptime(str(self.updated_at), "%Y-%m-%d %H:%M:%S.%f")
        )
        return dictJson
