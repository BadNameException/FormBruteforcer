#TODO: Make the generator save the passwords to a file, so that they can be more quickly accessed later


class Test:
    passwordDictionary = []
    charList = "abcdefghijklmnopqrstuwxkyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self):
        self.generatePasswords()
        self.printPasswords()

    def generatePasswords(self):
        for current in range(8):
            self.passwordDictionary = [i for i in self.charList]
            for y in range(current):
                self.passwordDictionary = [current + i for i in self.charList for current in self.passwordDictionary]

    def printPasswords(self):
        for i in self.passwordDictionary:
            print(i)
