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

    #Test1 if user is initialized
    def test_init(self):
        self.assertEqual(self.new_user.username,"janedoe")
        self.assertEqual(self.new_user.password,"j@Z3603")
        self.assertEqual(self.new_user.credentials,[])

    #Test2 to check if user is saved
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    #Test3 to check if we can have multiple users
    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()

        self.assertEqual(len(User.user_list),2)

    #Test4 if a user can be deleted
    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()
        test_user.delete_user()

        self.assertEqual(len(User.user_list),1)

    #Test5 Check if user exists
    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()

        user_exist = User.user_exists("johndoe")
        self.assertTrue(user_exist)

    #Test6 Find a particular user
    def test_find_user(self):
        self.new_user.save_user()
        test_user = User("johndoe","J0hzpO3",[])
        test_user.save_user()

        find_user = User.find_user("johndoe")
        self.assertEqual(find_user, test_user.username)


if __name__ == '__main__':
    unittest.main()
