# Introduction 

[Selenium](https://www.selenium.dev/) is a popular choice for black-box testing of web apps by simulating user interactions and veryfing the expected output. Selenium works with different browsers and it can help with tedius tasks such as entering text in input form fields, making selections, navigating menus, or clicking on buttons. 

# Setup

Begin by creating (and activating) a virtual environment. Next, install the packages described below. 

```
pip3 install flask flask-login flask-wtf flask-sqlalchemy selenium
```

Next, make sure you are able to run the web app in **src/app**. Create a user with id='Bob' and password='1'. Leave the web app running. 

# Black-box Testing with Selenium 

Open **tests/signin_test.py** and make sure Selenium is configured to use the correct browser, according to your environment. Then run the test case. Make sure to pass all 3 tests. Complete the tests that are incomplete. When you are done, finish **tests/signup_test.py**. 