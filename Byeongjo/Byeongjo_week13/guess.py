class Guess:

    def __init__(self, word):
        self.secretWord = word # 비밀단어
        self.guessedChars = [] # 사용한 글자를 담는 리스트
        self.numTries = 0 # 실패 횟수
        self.current= [] # 현재 상태 데이터를 담는 리스트
        for i in range(len(self.secretWord)) :
            self.current.append("_ ")

    def display(self):
        self.currentStatus = "" # 현재 맞춘 글자들을 표시
        for i in self.current :
            self.currentStatus += i
        self.used = "" # 현재 사용된 글자들을 표시
        for i in self.guessedChars :
            self.used += " " + i
        print("Current: " + self.currentStatus)
        print("Tries:", self.numTries)
        print("Already Used:", self.used)

    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord :
            for i in range(len(self.secretWord)) :
                if self.secretWord[i] == character :
                    self.current[i] = character
                    if not("_ " in self.current) :
                        return True
        else :
            self.numTries += 1
            return False