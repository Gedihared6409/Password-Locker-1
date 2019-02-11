import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credential("0788312907jk","twitter","kayitesijackie","0788312907jk")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.view_password,"0788312907jk")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.login,"kayitesijackie")
        self.assertEqual(self.new_credential.password,"0788312907jk")