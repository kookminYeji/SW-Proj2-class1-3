import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        #self.showScoreDB()

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        nameL = QLabel("Name")
        ageL = QLabel("Age")
        scoL = QLabel("Score")
        amuL = QLabel("Amount")
        retL = QLabel("Result")
        keyL = QLabel("Show Sort KEY")



        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoEdit = QLineEdit()
        self.amuEdit = QLineEdit()

        self.retEdit = QTextEdit(self)
        self.strret =""
        # retEdit.str = "zzzz"
        # retEdit.setText(retEdit.str)

        add = QPushButton("Add", self)
        dele = QPushButton("Del", self)
        find = QPushButton("Find", self)
        inc = QPushButton("Inc", self)
        show = QPushButton("show", self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(nameL)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(ageL)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(scoL)
        hbox.addWidget(self.scoEdit)
        hbox.addWidget(amuL)
        hbox.addWidget(self.amuEdit)

        h2box = QHBoxLayout()
        h2box.addWidget(add)
        h2box.addWidget(dele)
        h2box.addWidget(find)
        h2box.addWidget(inc)
        h2box.addWidget(show)

        keyHbox = QHBoxLayout()
        keyHbox.addWidget(keyL)

        h3box = QHBoxLayout()
        h3box.addWidget(retL)
        h3box.addWidget(self.retEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(h2box)
        vbox.addLayout(keyHbox)
        vbox.addLayout(h3box)
        self.setLayout(vbox)

        self.combo = QComboBox(self)
        self.combo.addItem("Name")
        self.combo.addItem("Age")
        self.combo.addItem("Score")
        self.combo.move(395, 60)

        add.clicked.connect(self.addC)
        dele.clicked.connect(self.deleC)
        find.clicked.connect(self.findC)
        inc.clicked.connect(self.incC)
        show.clicked.connect(self.showC)


        self.show()

    def addC(self):
        scdb = self.readScoreDB()
        record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoEdit.text()}
        scdb += [record]
        self.writeScoreDB()
        self.showScoreDB()

    def deleC(self):
        scdb = self.readScoreDB()
        rml = []
        for p in scdb:
            if p['Name'] == self.nameEdit.text():
                rm = scdb.index(p)
                rml.append(rm)
                del (scdb[rm])
                scdb.insert(rm, rm)
        for i in rml:
            scdb.remove(i)
        self.writeScoreDB()
        self.showScoreDB()

    def findC(self):
        self.retEdit.clear()  #결과창에 나온 텍스트 초기화
        self.strret = ""
        scdb = self.readScoreDB()
        for p in scdb:
            if self.nameEdit.text() == p['Name']:
                for key in p:
                    self.strret += key + "=" + str(p[key]) + ' '
                self.strret += '\n'
                self.retEdit.setText(self.strret )

    def incC(self):
        scdb = self.readScoreDB()
        for p in scdb:
            if  self.nameEdit.text() == p['Name']:
                plusScore = self.amuEdit.text()
                plusScore = int(plusScore)
                p['Score'] +=plusScore
                self.writeScoreDB()
                self.showScoreDB()
    def showC(self):
        keyname = self.combo.currentText()
        self.retEdit.clear()
        self.strret = ""
        scdb = self.readScoreDB()
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in p:
                self.strret += attr + " = " + str(p[attr]) + '   '
            self.strret += '\n'
        self.retEdit.setText(self.strret)






    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scdb = []
            return

        try:
            self.scdb = pickle.load(fH)
        except:
            QMessageBox.about(self, "message", "빈 파일")
        else:
            for x in self.scdb:
                x['Age'] = int(x['Age'])
                x['Score'] = int(x['Score'])
            fH.close()
            return self.scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self):

        self.retEdit.clear()
        self.strret = ""
        scdb = self.readScoreDB()
        for p in scdb:#sorted(scdb, key=lambda person: person["Name"]):
            for attr in p:
                self.strret += attr + "=" + str(p[attr]) + ' '
            self.strret +='\n'
        self.retEdit.setText(self.strret)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





