#!/usr/bin/python3
<<<<<<< HEAD
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model, amenity, city, place, review, state, user
from datetime import datetime
=======


""" Convert the dictionary representation to a JSON string """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
>>>>>>> parent of 6bc3c0a... initial checks

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json

<<<<<<< HEAD

class FileStorage:
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
=======
class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances """
    __file_path = "file.json"
>>>>>>> parent of 6bc3c0a... initial checks
    __objects = {}
    lavel_dict = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                  "City": City, "Place": Place, "State": State,
                  "Review": Review}

    def all(self):
<<<<<<< HEAD
        """returns private attribute: __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
        except Exception:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage.__objects[o_id] = FileStorage.CNC[k_cls](**d)
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
