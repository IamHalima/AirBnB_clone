#!/usr/bin/python3
<<<<<<< HEAD
"""
Place Class from Models Module
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Place class handles all application places"""

=======
""" Places where host the user's """
from . base_model import BaseModel


class Place(BaseModel):
    """ Places where we offer our services """
>>>>>>> parent of 6bc3c0a... initial checks
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ['', '']

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
