#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

<<<<<<< HEAD
    def setUp(self):
<<<<<<< HEAD
        """initializes new user for testing"""
        self.user = User()

    def test_instantiation(self):
        """... checks if User is properly instantiated"""
        self.assertIsInstance(self.user, User)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.user)
        my_list = ['User', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        self.user = User()
        my_str = str(self.user)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.user.save()
        actual = type(self.user.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.user_json = self.user.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.user_json)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value User"""
        self.user_json = self.user.to_json()
        actual = None
        if self.user_json['__class__']:
            actual = self.user_json['__class__']
        expected = 'User'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.user.email = "bettyholbertn@gmail.com"
        if hasattr(self.user, 'email'):
            actual = self.user.email
        else:
            actual = ''
        expected = "bettyholbertn@gmail.com"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main
=======
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""

        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of User class."""
        attributes = storage.attributes()["User"]
        o = User()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
>>>>>>> parent of 73da16d... initial checks
=======
import unittest
from models.base_model import BaseModel
from models.user import User
from io import StringIO
import sys
import datetime


class TestUser(unittest.TestCase):
    '''
        Testing User class
    '''

    def test_User_inheritance(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_User_attributes(self):
        '''
            Test the user attributes exist
        '''

        new_user = User()
        self.assertTrue("email" in new_user.__dir__())
        self.assertTrue("first_name" in new_user.__dir__())
        self.assertTrue("last_name" in new_user.__dir__())
        self.assertTrue("password" in new_user.__dir__())

    def test_type_email(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    def test_type_first_name(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_type_last_name(self):
        '''
            Test the type of last_name
        '''
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_type_password(self):
        '''
            Test the type of password
        '''
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)
>>>>>>> parent of 492c7bb... initial checks
