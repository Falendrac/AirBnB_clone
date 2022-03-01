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
