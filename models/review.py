#!/usr/bin/python3
<<<<<<< HEAD
"""
Review Class from Models Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class handles all application reviews"""

    place_id = ''
    user_id = ''
    text = ''

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
