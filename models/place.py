#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
"""
Place Class from Models Module
"""

=======
"""Defines the Place class."""
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        city_id (str): The City id.
        user_id (str): The User id.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        max_guest (int): The maximum number of guests of the place.
        price_by_night (int): The price by night of the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (list): A list of Amenity ids.
    """

<<<<<<< HEAD
<<<<<<< HEAD
=======
""" Places where host the user's """
from . base_model import BaseModel


class Place(BaseModel):
    """ Places where we offer our services """
>>>>>>> parent of 6bc3c0a... initial checks
=======
>>>>>>> parent of 647751d... initial checks
    city_id = ''
    user_id = ''
    name = ''
    description = ''
=======
    city_id = ""
    user_id = ""
    name = ""
    description = ""
>>>>>>> parent of 492c7bb... initial checks
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
