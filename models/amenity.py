#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""
Amenity Class from Models Module
"""

=======
"""Defines the Amenity class."""
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
=======
""" The amenities of place """
from . base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity (Comodidades) """
    name = ''
>>>>>>> parent of 6bc3c0a... initial checks
=======
    name = ""
>>>>>>> parent of 492c7bb... initial checks
