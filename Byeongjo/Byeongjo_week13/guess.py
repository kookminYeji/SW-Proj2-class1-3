class Guess:

    def __init__(self, word):
        self.secretWord = word # 비밀단어
        self.guessedChars = [] # 사용한 글자를 담는 리스트
        self.numTries = 0 # 실패 횟수
        self.current= [] # 현재 상태 데이터를 담는 리스트
        self.currentStatus = ""
        for i in range(len(self.secretWord)) :
            self.current.append("_ ")

    def display(self):
        self.currentStatus = "".join(self.current)  # 현재 맞춘 글자들을 표시
        self.used = ""
        self.used += " ".join(self.guessedChars) # 현재 사용된 글자들을 표시
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
        self.numTries += 1
        return False