#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
"""
Review Class from Models Module
"""

=======
"""Defines the Review class."""
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
=======
""" review of user's when left the place """
from . base_model import BaseModel


class Review(BaseModel):
    """ review of the user (qualification)"""
    place_id = ''
    user_id = ''
    text = ''
>>>>>>> parent of 6bc3c0a... initial checks
=======
    place_id = ""
    user_id = ""
    text = ""
>>>>>>> parent of 492c7bb... initial checks
