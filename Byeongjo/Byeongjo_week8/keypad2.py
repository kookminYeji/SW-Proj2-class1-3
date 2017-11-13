import calcFunctions


numPadList = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]

operatorList = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C',
]

constantList = [
    'pi',
    '빛의 이동 속도 (m/s)',
    '소리의 이동 속도 (m/s)',
    '태양과의 평균 거리 (km)',
]

functionList = [
    'factorial (!)',
    '-> binary',
    'binary -> dec',
    '-> roman',
]

def constant(calc, key) :
    if key == 'pi' :
        if calc.display.text() == "" :
            calc.display.setText('3.141592')
        else :
            calc.display.setText(calc.display.text() + "*" + "3.141592")
    elif key == '빛의 이동 속도 (m/s)':
        if calc.display.text() == "" :
            calc.display.setText('3E+8')
        else :
            calc.display.setText(calc.display.text() + "*" + "3E+8")
    elif key == '소리의 이동 속도 (m/s)':
        if calc.display.text() == "" :
            calc.display.setText('340')
        else :
            calc.display.setText(calc.display.text() + "*" + "340")
    elif key == '태양과의 평균 거리 (km)':
        if calc.display.text() == "" :
            calc.display.setText('1.5E+8')
        else :
            calc.display.setText(calc.display.text() + "*" + "1.5E+8")

def function(calc, key) :
    if key == 'factorial (!)':
        n = calc.display.text()
        value = calcFunctions.factorial(n)
        calc.display.setText(str(value))
    elif key == '-> binary':
        n = calc.display.text()
        value = calcFunctions.decToBin(n)
        calc.display.setText(str(value))
    elif key == 'binary -> dec':
        n = calc.display.text()
        value = calcFunctions.binToDec(n)
        calc.display.setText(str(value))
    elif key == '-> roman':
        n = calc.display.text()
        value = calcFunctions.decToRoman(n)
        calc.display.setText(str(value))
