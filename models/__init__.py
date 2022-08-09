<<<<<<< HEAD
from models.engine import file_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

storage = file_storage.FileStorage()
=======
#!/usr/bin/python3
""" create a unique FileStorage instance for your application """

from models.engine.file_storage import FileStorage

storage = FileStorage()
>>>>>>> parent of 6bc3c0a... initial checks
storage.reload()
CNC = file_storage.FileStorage.CNC
