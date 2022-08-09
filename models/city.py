#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
<<<<<<< HEAD
=======
#!/user/bin/python3
""" City where user's come from """
from . base_model import BaseModel


class City(BaseModel):
    """ city of the user """
    state_id = ''
    name = ''
>>>>>>> parent of 6bc3c0a... initial checks
=======
    state_id = ""
    name = ""
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
