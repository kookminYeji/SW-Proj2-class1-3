from time import *

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def interfibo(n):
    n1= 0
    n2 = 0
    for i in range(1, n+1):
        if i == 1:
            n1 = 1
        if i == 2:
            n2 = 1
        else:
            if not(i % 2 == 0):
                n1 = n1 + n2 
                ret = n1
            else:
                n2 = n1 + n2
                ret = n2
    return ret
while True:
    try:
        n = int(input("n : "))
    except ValueError:
        print("ValueError")
    else:
        if n <= 0:
            print("Break")
            break
        else:
            ts = time()
            interfibo(n)
            ts = time() - ts
            print("비재귀 n = %d, result : %d, time = %.6f" %(n, interfibo(n), ts))
            ts = time()
            fibo(n)
            ts = time() - ts
            print("재귀 n = %d, result : %d, time = %.6f" %(n, fibo(n), ts))
            
