mport unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
'''
Test class that defines test cases for the user class behaviours.
Args:
   unittest.TestCase: helps in creating test cases
'''
def setUp(self):
'''
Function to create a user account before each test
'''
self.new_user = User('John','Op\'an\'a','pswd100')
