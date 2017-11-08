from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def buttonClicked(self):
        button = calc.sender()
        key = button.text()
        if key == "=":
            try :
                result = str(eval(calc.display.text()))
            except SyntaxError :
                calc.display.setText("Error")
            else :
                calc.display.setText(result)
        elif key == "C":
            calc.display.setText("")
        else:
            if calc.display.text() == '0' :
                calc.display.setText(key)
            else :
                calc.display.setText(calc.display.text() + key)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [Button(str(x), Button.buttonClicked) for x in range(0, 10)]  # assignment 1
        # . and = Buttons
        self.decButton = Button('.', Button.buttonClicked)
        self.eqButton = Button('=', Button.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*', Button.buttonClicked)
        self.divButton = Button('/', Button.buttonClicked)
        self.addButton = Button('+', Button.buttonClicked)
        self.subButton = Button('-', Button.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(', Button.buttonClicked)
        self.rparButton = Button(')', Button.buttonClicked)

        # Clear Button
        self.clearButton = Button('C', Button.buttonClicked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        
        for i in range(1,10) :
            if i == 3 :
                numLayout.addWidget(self.digitButton[i], 2, 2)
            elif i < 3 :
                numLayout.addWidget(self.digitButton[i], 2, i%3-1)
            elif i == 6 :
                numLayout.addWidget(self.digitButton[i], 1, 2)
            elif i < 6 :
                numLayout.addWidget(self.digitButton[i], 1, i%3-1)
            elif i == 9 :
                numLayout.addWidget(self.digitButton[i], 0, 2)
            else :
                numLayout.addWidget(self.digitButton[i], 0, i%3-1)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())