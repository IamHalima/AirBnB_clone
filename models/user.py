#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""
User Class from Models Module
"""

=======
"""Defines the User class."""
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

<<<<<<< HEAD
=======
""" First User in ABNB project """
from . base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
>>>>>>> parent of 6bc3c0a... initial checks
    email = ''
    password = ''
    first_name = ''
    last_name = ''
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
=======
>>>>>>> parent of 6bc3c0a... initial checks
=======
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
>>>>>>> parent of 492c7bb... initial checks
