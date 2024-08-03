class password:
    def __init__(self, password): #constructor
        #initializing variable sfor length and for the alphabet/numbers
        self.leng = len(password) 
        self.password = password
        self.alphabetlow = 'abcdefghijklmnopqurstuvwxyz'
        self.alphabethigh = self.alphabetlow.upper()
        self.numbers = '1234567890'
    def num_special_char(self):
        #when called, it returns the amount of special characters (characters that arent numbers or in the alphabet) 
        counter = 0
        for char in range(self.leng):
            letter = self.password[char-1]
            if letter not in self.alphabethigh and letter not in self.alphabetlow and letter not in self.numbers:
                counter += 1
        return counter
    def num_capital_letters(self):
        #When called, it returns the number of capital letters
        counter = 0
        for char in range(self.leng):
            character = self.password[char-1]
            if character in self.alphabethigh:
                counter+=1
        return counter
    def num_lowercase_letters(self):
        #when called, it returns the number of lowercase letters
        counter = 0
        for char in range(self.leng):
            character = self.password[char-1]
            if character in self.alphabetlow:
                counter += 1
        return counter
    def num_numbers(self):
        #when called, it returns the number of numbers
        counter = 0
        for char in range(self.leng):
            character = self.password[char-1]
            if character in self.numbers:
                counter += 1
        return counter
    def length(self):
        #returns the length of the passcode
        return self.leng
    def getword(self):
        #returns the word
        return self.password
