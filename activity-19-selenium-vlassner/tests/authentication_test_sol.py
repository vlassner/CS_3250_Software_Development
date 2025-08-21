'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity 19 - Authentication Tests
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSignup(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.browser = webdriver.Edge()
        self.browser.get('http://localhost:5000')

    def testANumberOfButtons(self):
        buttons = self.browser.find_elements(By.TAG_NAME, 'button')
        self.assertEqual(2, len(buttons))

    def testBSignupFailure(self):
        signupButton = self.browser.find_elements(By.TAG_NAME, 'button')[1]
        signupButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('test_user')
        name = self.browser.find_element(By.ID, 'name')
        self.assertIsNotNone(name)
        name.send_keys('Test User')
        about = self.browser.find_element(By.ID, 'about')
        self.assertIsNotNone(about)
        about.send_keys('...')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('12345678')
        passwd_confirm = self.browser.find_element(By.ID, 'passwd_confirm')
        self.assertIsNotNone(passwd_confirm)
        passwd_confirm.send_keys('1234567')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        error_text = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertEqual('Passwords do not match!', error_text.text)

    def testBSignupSuccess(self):
        signupButton = self.browser.find_elements(By.TAG_NAME, 'button')[1]
        signupButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('test_user')
        name = self.browser.find_element(By.ID, 'name')
        self.assertIsNotNone(name)
        name.send_keys('Test User')
        about = self.browser.find_element(By.ID, 'about')
        self.assertIsNotNone(about)
        about.send_keys('...')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('12345678')
        passwd_confirm = self.browser.find_element(By.ID, 'passwd_confirm')
        self.assertIsNotNone(passwd_confirm)
        passwd_confirm.send_keys('12345678')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()

    def testBSignInFailure(self):
        signinButton = self.browser.find_elements(By.TAG_NAME, 'button')[0]
        signinButton.click()
        id = self.browser.find_element(By.ID, 'id')
        self.assertIsNotNone(id)
        id.send_keys('test_user')
        passwd = self.browser.find_element(By.ID, 'passwd')
        self.assertIsNotNone(passwd)
        passwd.send_keys('1234567')
        submit = self.browser.find_element(By.ID, 'submit')
        submit.click()
        error_text = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertEqual('Wrong Password!', error_text.text)
            
if __name__ == '__main__':
    unittest.main()