import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB(self.scoredb, "Name")

    def initUI(self):

        # Label
        name = QLabel("Name: ")
        age = QLabel("Age: ")
        score = QLabel("Score: ")
        amount = QLabel("Amount: ")
        key = QLabel("Key: ")
        result = QLabel("Result: ")

        # title
        self.nametitle = QLineEdit()
        self.agetitle = QLineEdit()
        self.scoretitle = QLineEdit()
        self.amounttitle = QLineEdit()
        self.key_comboBox = QComboBox()
        self.key_comboBox.addItem("Name")
        self.key_comboBox.addItem("Age")
        self.key_comboBox.addItem("Score")
        self.resulttitle = QTextEdit()

        # button
        Add = QPushButton("Add")
        Del = QPushButton("Del")
        Find = QPushButton("Find")
        Inc = QPushButton("Inc")
        Show = QPushButton("Show")

        # hbox1
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(name)
        hbox1.addWidget(self.nametitle, 15)
        hbox1.addWidget(age)
        hbox1.addWidget(self.agetitle, 15)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scoretitle, 15)

        # hbox2
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amounttitle)
        hbox2.addWidget(key)
        hbox2.addWidget(self.key_comboBox)

        # hbox3
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(Add)
        hbox3.addWidget(Del)
        hbox3.addWidget(Find)
        hbox3.addWidget(Inc)
        hbox3.addWidget(Show)

        # hbox4
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(result, 100)

        # hbox5
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addWidget(self.resulttitle, 100)

        # vbox1
        vbox1 = QVBoxLayout()
        vbox1.addStretch(1)
        vbox1.addLayout(hbox1)
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)
        vbox1.addLayout(hbox5)

        self.setLayout(vbox1)

        # when button clicked
        Add.clicked.connect(self.addInfo)
        Del.clicked.connect(self.delInfo)
        Find.clicked.connect(self.findInfo)
        Inc.clicked.connect(self.incInfo)
        Show.clicked.connect(self.showInfo)

        # 위치, 윈도우 타이틀
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    # Add 함수 점수와 나이에 텍스트가 들어갔을 때
    def addInfo(self):
        nametext = self.nametitle.text()
        if nametext == "":
            nametext = "None"
        agetext = self.agetitle.text()
        if agetext == "":
            agetext = 0
        scoretext = self.scoretitle.text()
        if scoretext == "":
            scoretext = 0
        try:
            self.scoredb.append({"Name": nametext, "Age": int(agetext), "Score": int(scoretext)})
        except ValueError:
            self.resulttitle.setText("Wrong Type")
        else:
            self.showScoreDB(self.scoredb, "Name")

    # Del 함수
    def delInfo(self):
        text = self.nametitle.text()
        self.reverse_scoredb = sorted(self.scoredb, key=lambda x: x["Name"], reverse=True)
        for i in self.reverse_scoredb:
            if i["Name"] == text:
                self.scoredb.remove(i)
        self.showScoreDB(self.scoredb, "Name")

    # Find 함수
    def findInfo(self):
        text = self.nametitle.text()
        findName = []
        for i in self.scoredb:
            if i["Name"] == text:
                findName.append(i)
        if len(findName) == 0:
            self.resulttitle.setText("I can't find this name")
        else:
            self.showScoreDB(findName, "Name")

    # Inc 함수
    def incInfo(self):
        text = self.nametitle.text()
        score = self.amounttitle.text()
        if score == "":
            score = 0
        for i in self.scoredb:
            if i["Name"] == text:
                i["Score"] += int(score)
        self.showScoreDB(self.scoredb, "Name")

    # Show 함수
    def showInfo(self):
        Info = self.key_comboBox.currentText()
        self.showScoreDB(self.scoredb, Info)

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self, scoredb, keyname):
        Info = ""
        for p in sorted(scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                Info += attr
                Info += "="
                Info += str(p[attr]) + " "
            Info += "\n"
        self.resulttitle.setText(Info)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
