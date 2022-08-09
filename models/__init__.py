<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

storage = file_storage.FileStorage()
<<<<<<< HEAD
<<<<<<< HEAD
=======
#!/usr/bin/python3
""" create a unique FileStorage instance for your application """

from models.engine.file_storage import FileStorage

storage = FileStorage()
>>>>>>> parent of 6bc3c0a... initial checks
=======
#!/usr/bin/python3
"""__init__ magic method for models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
storage.reload()
