#!/usr/bin/python3
"""
module user
"""


from models.base_model import BaseModel


class User(BaseModel):
    """
    The user for AirBnB
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __str__(self):
        """
        Create a representation of the str
        """
        return f"[User] ({self.id}) {self.__dict__}"
