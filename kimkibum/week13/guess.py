class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = list()
        self.numTries = 0
        self.currentWord = '_' * len(word)  # 몇자리 글자인지 확인하기 어려움
        self.guessedChars = ''



    def display(self):
        print('word length :' ,len(self.secretWord)) #몇자리인지 잘 구분이 안가서 추가함
        print("Current : ", self.currentWord)
        print("Already Used : " , self.guessedChars)
        print("Tries : " , self.numTries)


    def guess(self, character):
        self.guessedChars += character + ', '
        if not(character  in self.secretWord):
            self.numTries += 1
            return False
        else:
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    currentwordlist = list(self.currentWord)
                    del currentwordlist[i]
                    currentwordlist.insert(i,character)
                    self.currentWord = ''.join(currentwordlist)

        if self.currentWord == self.secretWord:
            return True

        else:
            return False
