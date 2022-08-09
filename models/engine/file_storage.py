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
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime
<<<<<<< HEAD
<<<<<<< HEAD
=======


""" Convert the dictionary representation to a JSON string """
import json
import os
=======
"""Defines the FileStorage class."""
import json
>>>>>>> parent of 492c7bb... initial checks
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> parent of 6bc3c0a... initial checks
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json
=======
from models.place import Place
from models.amenity import Amenity
from models.review import Review
>>>>>>> parent of 492c7bb... initial checks


class FileStorage:
<<<<<<< HEAD
    """handles long term storage of all class instances"""
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    __file_path = './dev/file.json'
<<<<<<< HEAD
<<<<<<< HEAD
=======
class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
>>>>>>> parent of 6bc3c0a... initial checks
=======
    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
    __objects = {}

    def all(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
=======
    __objects = {}

    def all(self):
>>>>>>> parent of 647751d... initial checks
        """returns private attribute: __objects"""
=======
        """Return the dictionary __objects."""
>>>>>>> parent of 492c7bb... initial checks
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
<<<<<<< HEAD
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)
<<<<<<< HEAD
<<<<<<< HEAD
=======
        """ returns the dictionary __objects """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists, otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised) """
        # Validate if file exists
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    # Separate name_class from id and split the separator
                    k = key.split('.')
                    # search "__class__": "BaseModel"
                    class_name = k[0]
                    # set in __objects the key, value
                    self.new(eval("{}".format(class_name))(**value))
>>>>>>> parent of 6bc3c0a... initial checks
=======
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
