#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
<<<<<<< HEAD
=======


""" Base module """
import uuid
>>>>>>> parent of 6bc3c0a... initial checks
=======
"""Defines the BaseModel class."""
import models
from uuid import uuid4
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
from datetime import datetime


class BaseModel:
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
    """attributes and functions for BaseModel class"""
=======
    """Represents the BaseModel of the HBnB project."""
>>>>>>> parent of 492c7bb... initial checks

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
<<<<<<< HEAD
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)
<<<<<<< HEAD
=======
    """ class for all other classes to inherit from """
    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if len(kwargs) > 0:
            # each key of this dictionary is an attribute name
            # each value of this dictionary is the value of this attribute name
            for key, value in kwargs.items():
                if key == "updated_at":
                    # Convert string date to datetime object
                    # strptime (string parse time): Parse a string into a -
                    # datetime object given a corresponding format
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    # This happens because __class__ is not mandatory in output
                    continue

                setattr(self, key, value)
        else:
            # Generate a random UUID
            self.id = str(uuid.uuid4())
            # assign with the current datetime when an instance is created
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # if it’s a new instance add a call to the method new(self) on stge
            models.storage.new(self)

    def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        # Old-style: self.__class__.__name__
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return (mssg)

    # Public instance methods
    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        # Define a dictionary and key __class__ that add to this dictionary
        # with the class name of the object
        tdic = {}
        tdic["__class__"] = type(self).__name__
        # loop over dict items and validate created_at and updated_at to
        # convert in ISO format
        for n, i in self.__dict__.items():
            if isinstance(i, datetime):
                tdic[n] = i.isoformat()
            else:
                tdic[n] = i
        return (tdic)
>>>>>>> parent of 6bc3c0a... initial checks
=======
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
