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


if __name__ == '__main__':
    unittest.main()