"""
BDD - Basis of our tests
1. Create a credential
2. Save a credential
3. Display credential
4. Delete credential
    *Credential should have:
        a.)Name of the account
        b.)Username
        c.)Email address
        d.)Password
"""

import unittest #test framework
from credentials import Credential #import class

class TestCredential(unittest.TestCase):
    # Create credential object
    def setUp(self):
        self.new_credential = Credential(
            "Twitter","janedoe","jane@example.com","J@n3%2D0#"
        )

    # Teardown mthd resets credential list after every testcase
    def tearDown(self):
        Credential.credential_list = []

    # Testcase1 - Test if object is initialized properly
    def test_init(self):
        self.assertEqual(self.new_credential.account,"Twitter")
        self.assertEqual(self.new_credential.username,"janedoe")
        self.assertEqual(self.new_credential.email,"jane@example.com")
        self.assertEqual(self.new_credential.password,"J@n3%2D0#")

if __name__ == '__main__':
    unittest.main()