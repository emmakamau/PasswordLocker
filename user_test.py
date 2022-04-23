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

    #Test if user is initialized
    def test_init(self):
        self.assertEqual(self.new_user.username,"janedoe")
        self.assertEqual(self.new_user.password,"j@Z3603")
        self.assertEqual(self.new_user.credentials,[])

if __name__ == '__main__':
    unittest.main()
