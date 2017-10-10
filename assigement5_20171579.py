import time

def fibo(n):
    if n <= 1 :
        return n
    else :
        first, second = 1, 1

        for i in range(n-1):
            first, second = second, first+second

        return first

def fibo_recursive(n):
    if n <= 1 :
        return n
    else :
        return fibo_recursive(n-1) + fibo_recursive(n-2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo_recursive(nbr)
    ts = time.time() - ts
    print("fibo_recursive(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
