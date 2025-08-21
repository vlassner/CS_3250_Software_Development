'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity 19 - Sign-up Test Case
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# pre-condition: a user with id="jane" does NOT exist
# post-condition: the user is created
class SignupTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        # self.browser = webdriver.Edge()
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:5000/')

    def testSucessfulSignup(self):
        pass

    def testUnsucessfulSignupIdExists(self):
        pass

    def testUnsucessfulSignupPasswordsDontMach(self):
        pass

if __name__ == '__main__':
    unittest.main()