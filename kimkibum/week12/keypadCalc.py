from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'

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

constant = {
	'pi' : '3.141592', 
	'빛의 이동 속도 (m/s)' : '3E+8',
	'소리의 이동 속도 (m/s)' : '340',
	'태양과의 평균 거리 (km)' : '1.5E+8',}


function = {
	'factorial (!)' : factorial,
	'-> binary' : decToBin,
	'binary -> dec' : binToDec,
	'-> roman' : decToRoman}

