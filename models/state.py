#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
"""
State Class from Models Module
"""

=======
"""Defines the State class."""
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel


class State(BaseModel):
    """Represent a state.

    Attributes:
        name (str): The name of the state.
    """

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
<<<<<<< HEAD
<<<<<<< HEAD
=======
""" State where user's come from """
from . base_model import BaseModel


class State(BaseModel):
    """ Define the state of the user """
    name = ''
>>>>>>> parent of 6bc3c0a... initial checks
=======
    name = ""
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
