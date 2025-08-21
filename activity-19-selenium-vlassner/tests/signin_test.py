'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity 19 - Sign-in Test Case
'''

import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By

# pre-condition: a user with id="bob" and password="1" already exists; 
# a user with id="jane" does NOT exist
class SigninTest(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.browser = webdriver.Edge()
        # self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:5000/')

    def testSucessfulSignin(self):
        signinButton = self.browser.find_elements(By.TAG_NAME, 'button')[0]
        signinButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('bob')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('1')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        page = self.browser.current_url
        self.assertEqual('http://localhost:5000/users', page)

    def testUnsucessfulSigninWrongId(self):
        signinButton = self.browser.find_elements(By.TAG_NAME, 'button')[0]
        signinButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('jane')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('1')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        page = self.browser.current_url
        p = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertTrue(p.text.startswith('Could not find a user with the given id'))

    def testUnsucessfulSigninWrongPassword(self):
        signinButton = self.browser.find_elements(By.TAG_NAME, 'button')[0]
        signinButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('bob')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('2')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        page = self.browser.current_url
        p = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertTrue(p.text.startswith('Wrong password!'))

if __name__ == '__main__':
    unittest.main()