import time

def fibo(n):
    if n <= 1 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

try :
    n = int(input("Enter a number : "))
except ValueError :
    print("That's not integer")
else :
    ts = time.time()
    if n <= 1 :
        k = n
    else :
        k = 1
        num = 0
        i = 1
        while i < n :
            a = k #전값
            k = num + a #전값+전전값
            num = a #전전값
            i = i + 1
    ts = time.time() - ts
    print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, k, ts))

    ts2 = time.time()
    fibo_number = fibo(n)
    ts2 = time.time() - ts2
    print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, fibo_number, ts2))

"""
import time
def fibo(n):
    if n <= 1 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

n= int(input("Enter a number : "))
start = time.time()
if n <= 1 :
    k = n
else :
    number_list = [0]
    k = 1
    i = 0
    while i<n :
        if len(number_list) == 1 :
            b = number_list[i]
            c = b + k
            number_list.append(c)
        else :
            b = number_list[i-1]
            c = number_list[i]
            d = b + c
            number_list.append(d)
        i += 1
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, number_list[len(number_list)-1], time.time()-start))

start2 = time.time()
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, fibo(n), time.time()-start2))
"""
"""
import time

def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

def iterfibo(n):
    fibList = [0, 1]
    i = 2
    while True:
        if n < i:
            break
        fibList.append(fibList[i-2] + fibList[i-1])
        i += 1
    return fibList.pop()

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
"""
