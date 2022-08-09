#!/usr/bin/python3
<<<<<<< HEAD
"""
User Class from Models Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class handles all application users"""

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
