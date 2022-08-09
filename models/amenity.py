#!/usr/bin/python3
<<<<<<< HEAD
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class handles all application amenities"""

    name = ''

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
