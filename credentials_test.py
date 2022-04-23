"""
BDD - Basis of our tests
1. Create a credential
2. Save a credential
3. Save more than one credential
4. Display credential
5. Delete credential
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

    # Testcase2 - Test if object is saved
    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    # Testcase3 - Test if we can save multiple credentials
    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","JaneDoe","jane@example.com","jaN3@do3")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    # Testcase4 - Test if we can delete a credential
    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","JaneDoe","jane@example.com","jaN3@do3")
        test_credential.save_credential()

        test_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)

    # Testcase5 - Find credential by account name
    def test_find_credential_by_account(self):
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","JaneDoe","jane@example.com","jaN3@do3")
        test_credential.save_credential()

        found_account = Credential.find_by_account("Facebook")
        self.assertEqual(found_account,test_credential.account)

    # Testcase6 - Check if credential exists using account
    def test_credential_exist(self):
        self.new_credential.save_credential()
        test_credential = Credential("Facebook","JaneDoe","jane@example.com","jaN3@do3")
        test_credential.save_credential()

        credential_exist = Credential.credential_exist("Facebook")
        self.assertTrue(credential_exist)

    # Testcase7 - Display all credentials
    def test_display_all_credential(self):
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)

if __name__ == '__main__':
    unittest.main()