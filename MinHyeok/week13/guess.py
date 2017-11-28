class Guess:

    def __init__(self, word):

        self.numTries = 0

        self.wordlist = list(word)
        self.inputlist = []
        self.guessedChars = []
        self.secretWord = ""
        self.currentStatus = ""

        for i in range(len(self.wordlist)):
            self.inputlist.append("_")

    def display(self):

        print("Used:", " ".join(self.guessedChars))
        print("Current:", "".join(self.inputlist))
        print("Tries:",self.numTries)

    def guess(self, character):

        self.guessedChars.append(character)
        for i in range(len(self.wordlist)):
            if self.wordlist[i] == character:

                self.inputlist[i] = self.wordlist[i]
        if not character in self.wordlist:
            self.numTries += 1
        self.currentStatus = "".join(self.inputlist)
        self.secretWord = "".join(self.wordlist)
        if self.inputlist == self.wordlist:
            return True

        return False
