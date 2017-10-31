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
        self.showScoreDB()


    def initUI(self):
        name = QLabel("Name : ", self)
        age = QLabel("Age : ", self)
        score = QLabel("Score : ", self)
        self.nameBox = QLineEdit()
        self.ageBox = QLineEdit()
        self.scoreBox = QLineEdit()
        ######
        hBox = QHBoxLayout()
        hBox.addWidget(name)
        hBox.addWidget(self.nameBox)
        hBox.addWidget(age)
        hBox.addWidget(self.ageBox)
        hBox.addWidget(score)
        hBox.addWidget(self.scoreBox)
        #######
        amount = QLabel("Amount: ", self)
        key = QLabel("key:")
        #######
        self.amountBox = QLineEdit()
        self.key = QComboBox()
        self.key.addItem("Name")
        self.key.addItem("Score")
        self.key.addItem("Age")

        hBox_2line = QHBoxLayout()
        hBox_2line.addStretch(1)
        hBox_2line.addWidget(amount)
        hBox_2line.addWidget(self.amountBox)
        hBox_2line.addWidget(key)
        hBox_2line.addWidget(self.key)

        butadd = QPushButton("Add", self)
        butadd.clicked.connect(self.AddBtnClicked)
        butdel = QPushButton("Del", self)
        butdel.clicked.connect(self.DelBtnClicked)
        butfind = QPushButton("Find", self)
        butinc = QPushButton("Inc", self)
        butfind.clicked.connect(self.FindBtnClicked)
        butshow = QPushButton("Show", self)
        butshow.clicked.connect(self.ShowBtnClicked)
        hBox_3line = QHBoxLayout()
        hBox_3line.addWidget(butadd)
        hBox_3line.addWidget(butdel)
        hBox_3line.addWidget(butfind)
        hBox_3line.addWidget(butinc)
        hBox_3line.addWidget(butshow)

        result = QLabel("Result: ")
        self.textBox = QTextEdit(self)
        hBox_4line = QHBoxLayout()
        hBox_4line.addWidget(result)
        hBox_5line = QHBoxLayout()
        hBox_5line.addWidget(self.textBox)
        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox_2line)
        vBox.addLayout(hBox_3line)
        vBox.addLayout(hBox_4line)
        vBox.addLayout(hBox_5line)
        self.setLayout(vBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def ShowBtnClicked(self):
            self.showScoreDB(self.keyComboBox.currentText())

    def AddBtnClicked(self):
            record = {'Name': self.nameLineBox.text(), 'Age': int(self.ageLineBox.text()),
                      'Score': int(self.scoreLineBox.text())}
            self.scoredb += [record]
            self.showScoreDB()


    def DelBtnClicked(self):
        pass
        #try:
            #for p in reversed(scdb):
                #if p['Name'] == parse[1]:
                    #scdb.remove(p)


    def FindBtnClicked(self):
        pass

       # for name in scdb:
            #if name['Name'] == parse[1]:
             #   for sort in sorted(name):
              #      print(sort + "=" + name[sort], end=' ')
               # print()

    def IncBtnClicked(self):
        pass

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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

    def showScoreDB(self, keyname="Score"):
        temp = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.textBox.setText(temp)
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





