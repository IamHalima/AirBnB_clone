#!/usr/bin/python3
<<<<<<< HEAD
"""
State Class from Models Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class handles all application states"""

    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
=======
""" State where user's come from """
from . base_model import BaseModel


class State(BaseModel):
    """ Define the state of the user """
    name = ''
>>>>>>> parent of 6bc3c0a... initial checks
