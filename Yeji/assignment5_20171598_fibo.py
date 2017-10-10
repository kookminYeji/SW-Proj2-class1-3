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
    print(ts)
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print(ts)
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
