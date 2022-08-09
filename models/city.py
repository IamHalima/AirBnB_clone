<<<<<<< HEAD
#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class handles all application cities"""

    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
=======
#!/user/bin/python3
""" City where user's come from """
from . base_model import BaseModel


class City(BaseModel):
    """ city of the user """
    state_id = ''
    name = ''
>>>>>>> parent of 6bc3c0a... initial checks
