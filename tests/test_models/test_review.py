#!/usr/bin/python3

'''
    All the test for the user model are implemented here.
'''

<<<<<<< HEAD
<<<<<<< HEAD
=======

class TestReviewInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('........  Review  Class  ........')
        print('.................................\n\n')

>>>>>>> parent of 647751d... initial checks
    def setUp(self):
        """initializes new review for testing"""
        self.review = Review()

    def test_instantiation(self):
        """... checks if Review is properly instantiated"""
        self.assertIsInstance(self.review, Review)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.review)
        my_list = ['Review', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.review)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.review.save()
        actual = type(self.review.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.review_json = self.review.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.review_json)
        except Exception:
            actual = 0
        self.assertTrue(1 == actual)

    def test_json_class(self):
        """... to_json should include class key with value Review"""
        self.review_json = self.review.to_json()
        actual = None
        if self.review_json['__class__']:
            actual = self.review_json['__class__']
        expected = 'Review'
        self.assertEqual(expected, actual)

    def test_email_attribute(self):
        """... add email attribute"""
        self.review.text = "This place smells"
        if hasattr(self.review, 'text'):
            actual = self.review.text
        else:
            acual = ''
        expected = "This place smells"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main
<<<<<<< HEAD
<<<<<<< HEAD
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
        """Tests instantiation of Review class."""

        b = Review()
        self.assertEqual(str(type(b)), "<class 'models.review.Review'>")
        self.assertIsInstance(b, Review)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Review class."""
        attributes = storage.attributes()["Review"]
        o = Review()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)

if __name__ == "__main__":
    unittest.main()
>>>>>>> parent of 73da16d... initial checks
=======
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    '''
        Testing Review class
    '''

    def test_Review_inheritance(self):
        '''
            tests that the Review class Inherits from BaseModel
        '''
        new_review = Review()
        self.assertIsInstance(new_review, BaseModel)

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        self.assertTrue("place_id" in new_review.__dir__())
        self.assertTrue("user_id" in new_review.__dir__())
        self.assertTrue("text" in new_review.__dir__())

    def test_Review_attributes(self):
        '''
            Test that Review class has place_id, user_id and text
            attributes.
        '''
        new_review = Review()
        place_id = getattr(new_review, "place_id")
        user_id = getattr(new_review, "user_id")
        text = getattr(new_review, "text")
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)
>>>>>>> parent of 492c7bb... initial checks
=======
>>>>>>> parent of 647751d... initial checks
=======
>>>>>>> parent of 647751d... initial checks
