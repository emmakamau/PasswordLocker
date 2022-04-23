"""
BDD - Basis of our tests
1. We should be able to create a user.
2. Save the user
    * User has a username and password
    * Credentials from the credentials class
"""

import unittest
from user import User

class TestUser(unittest.TestCase):
    

    def setUp(self):
        self.new_user = User("janedoe","j@Z3603",[])

    def tearDown(self) -> None:
        User.user_list = []

    #Test if user is initialized
    def test_init(self):
        self.assertEqual(self.new_user.username,"janedoe")
        self.assertEqual(self.new_user.password,"j@Z3603")
        self.assertEqual(self.new_user.credentials,[])

    #Test to check if user is saved
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    #Test to check if we can have multiple users
    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    #Test if a user can be deleted
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()
        test_user.delete_user()

        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
