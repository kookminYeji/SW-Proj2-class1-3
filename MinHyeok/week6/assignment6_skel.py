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
         #첫번째 줄 UI 작성 후 첫번째 레이아웃으로 등록
        nameLabel = QLabel("Name:",self)
        self.nameLineBox = QLineEdit()
        ageLabel = QLabel("Age:",self)
        self.ageLineBox = QLineEdit()
        scoreLabel = QLabel("Score:",self)
        self.scoreLineBox = QLineEdit()

        hBox = QHBoxLayout()
        hBox.addWidget(nameLabel)
        hBox.addWidget(self.nameLineBox)
        hBox.addWidget(ageLabel)
        hBox.addWidget(self.ageLineBox)
        hBox.addWidget(scoreLabel)
        hBox.addWidget(self.scoreLineBox)
        
        #두번째 줄 UI 작성 후 두번째 레이아웃으로 등록
        spaceLabel = QLabel("               ",self)
        amountLabel = QLabel("Amount: ",self)
        self.amountLineBox = QLineEdit()
        keyLabel = QLabel("key:")
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItem("Name")
        self.keyComboBox.addItem("Score")
        self.keyComboBox.addItem("Age")



        hBox2 = QHBoxLayout()
        hBox2.addWidget(spaceLabel)
        hBox2.addWidget(amountLabel)
        hBox2.addWidget(self.amountLineBox)
        hBox2.addWidget(keyLabel)
        hBox2.addWidget(self.keyComboBox)

        #세번째 줄 UI 작성 후 세번째 레이아웃으로 등록
        spaceLabel2 = QLabel('                  ',self)
        addButton = QPushButton("Add",self)
        delButton = QPushButton("Del",self)
        findButton = QPushButton("Find",self)
        incButton = QPushButton("Inc",self)
        showButton = QPushButton("Show",self)

        addButton.clicked.connect(self.AddBtnClicked)
        delButton.clicked.connect(self.DelBtnClicked)
        findButton.clicked.connect(self.FindBtnClicked)
        incButton.clicked.connect(self.IncBtnClicked)
        showButton.clicked.connect(self.ShowBtnClicked)

        hBox3 = QHBoxLayout()
        hBox3.addWidget(spaceLabel2)
        hBox3.addWidget(addButton)
        hBox3.addWidget(delButton)
        hBox3.addWidget(findButton)
        hBox3.addWidget(incButton)
        hBox3.addWidget(showButton)

        #네번째 줄 UI 작성 후 네번째 레이아웃으로 등록
        resultLabel = QLabel("Result: ")

        hBox4 = QHBoxLayout()
        hBox4.addWidget(resultLabel)
        
        #다섯번째 줄 UI 작성 후 다섯번째 레이아웃으로 등록
        self.textBox = QTextEdit(self)

        hBox5 = QHBoxLayout()
        hBox5.addWidget(self.textBox)


        #수평 정렬 레이아웃을 수직으로 순서대로 배치
        vBox = QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox2)
        vBox.addLayout(hBox3)
        vBox.addLayout(hBox4)       
        vBox.addLayout(hBox5)
        self.setLayout(vBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('DataBaseManager')
        

        self.show()
   #Show 버튼을 눌렀을때 키값을 기준으로 정렬해 출력함
    def ShowBtnClicked(self):
        self.showScoreDB(self.keyComboBox.currentText())

    def AddBtnClicked(self):
        record = {'Name': self.nameLineBox.text(),'Age': int(self.ageLineBox.text()),'Score':int(self.scoreLineBox.text())}
        self.scoredb += [record]
        self.showScoreDB()

    def DelBtnClicked(self):
        reverse_scdb = sorted(self.scoredb,key=lambda x: x["Name"],reverse=True)
        for p in reverse_scdb:
            if p['Name'] == self.nameLineBox.text():
                self.scoredb.remove(p)
        self.showScoreDB()
    def FindBtnClicked(self):
        temp = ""
        for p in sorted(self.scoredb , key=lambda person: person["Name"]):        
            for attr in sorted(p):
                if p["Name"] == self.nameLineBox.text():
                    temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.textBox.setText(temp)      
    def IncBtnClicked(self):
        for p in sorted(self.scoredb , key=lambda person: person["Name"]):        
            for attr in sorted(p):
                if p["Name"] == self.nameLineBox.text():
                    p["Score"] += int(self.amountLineBox.text())
                    break;
        self.showScoreDB(); 



   #키입력 이벤트 처리
    def keyPressEvent(self,e):
        if e.key() == Qt.Key_Escape:
            self.close()

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
            for i in self.scoredb:
                i['Age'] = int(i['Age'])
                i['Score'] = int(i['Score'])
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self,keyname="Score"):
        temp = ""
        for p in sorted(self.scoredb , key=lambda person: person[keyname]):        
            for attr in sorted(p):
                temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.textBox.setText(temp)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()

    sys.exit(app.exec_())





