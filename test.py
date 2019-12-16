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

def test__init__(self):
'''
Test to if check the initialization/creation of user instances is properly done
'''
self.assertEqual(self.new_user.first_name,'John')
self.assertEqual(self.new_user.last_name,'Op\'an\'a')
self.assertEqual(self.new_user.password,'pswd100')

def test_save_user(self):
'''
Test to check if the new users info is saved into the users list
'''
self.new_user.save_user()
self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
'''
Test class that defines test cases for the credentials class behaviours.
Args:
   unittest.TestCase: helps in creating test cases
'''
def test_check_user(self):
'''
Function to test whether the login in function check_user works as expected
'''
self.new_user = User('John','Op\'an\'a','pswd100')
self.new_user.save_user()
user2 = User('Ken','Op\'an\'a','pswd100')
user2.save_user()

for user in User.users_list:
if user.first_name == user2.first_name and user.password == user2.password:
current_user = user.first_name
return current_user

self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))

def setUp(self):
'''
Function to create an account's credentials before each test
'''
self.new_credential = Credential('John','Facebook','johnopana','pswd100')

def test__init__(self):
'''
Test to if check the initialization/creation of credential instances is properly done
'''
self.assertEqual(self.new_credential.user_name,'John')
self.assertEqual(self.new_credential.site_name,'Facebook')
self.assertEqual(self.new_credential.account_name,'johnopana')
self.assertEqual(self.new_credential.password,'pswd100')

def test_save_credentials(self):
'''
Test to check if the new credential info is saved into the credentials list
'''
self.new_credential.save_credentials()
twitter = Credential('Harun','Twitter','johnopana','pswd100')
twitter.save_credentials()
self.assertEqual(len(Credential.credentials_list),2)

# def test_generate_password(self):
# '''
# Test to check if the generate password generates 8 character long alphanumeric numbers
# '''
# self.twitter = Credential('Twitter','maryjoe','')
# self.twitter.password = generate_password()
# self.assertEqual()

def tearDown(self):
'''