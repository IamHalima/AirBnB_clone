#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
<<<<<<< HEAD
from datetime import datetime
import models
import json

State = models.state.State
BaseModel = models.base_model.BaseModel


class TestStateDocs(unittest.TestCase):
    """Class for testing State docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   State Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nState Class from Models Module\n'
        actual = models.state.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'State class handles all application states'
        actual = State.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new state'
        actual = State.__init__.__doc__
        self.assertEqual(expected, actual)


class TestStateInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  State Class  .........')
        print('.................................\n\n')

    def setUp(self):
<<<<<<< HEAD
        """initializes new state for testing"""
        self.state = State()

    def test_instantiation(self):
        """... checks if State is properly instantiated"""
        self.assertIsInstance(self.state, State)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.state)
        my_list = ['State', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.state)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.state.save()
        actual = type(self.state.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.state_json = self.state.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.state_json)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value State"""
        self.state_json = self.state.to_json()
        actual = None
        if self.state_json['__class__']:
            actual = self.state_json['__class__']
        expected = 'State'
        self.assertEqual(expected, actual)

    def test_name_attribute(self):
        """... add name attribute"""
        self.state.name = "betty"
        if hasattr(self.state, 'name'):
            actual = self.state.name
        else:
            acual = ''
        expected = "betty"
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
        """Tests instantiation of State class."""

        b = State()
        self.assertEqual(str(type(b)), "<class 'models.state.State'>")
        self.assertIsInstance(b, State)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of State class."""
        attributes = storage.attributes()["State"]
        o = State()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
>>>>>>> parent of 73da16d... initial checks
=======
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
>>>>>>> parent of 492c7bb... initial checks
