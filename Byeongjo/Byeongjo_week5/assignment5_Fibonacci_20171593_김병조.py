import time

def fibo(n):
    if n <= 1 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number : "))
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
        i = i+1
ts = time.time() - ts
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, k, ts))

ts2 = time.time()
fibo_number = fibo(n)
ts2 = time.time()-ts2
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, fibo_number, ts2))

"""
import time
def fibo(n):
    if n <= 1 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)

n= int(input("Enter a number : "))
start = time.time()
number_list = [0]
k = 1
i = 0
while i<n :
    if len(number_list) == 1 :
        b = number_list[i]
        c = b+k
        number_list.append(c)
    else :
        b = number_list[i-1]
        c = number_list[i]
        d = b+c
        number_list.append(d)
    i+=1
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, number_list[len(number_list)-1], time.time()-start))

start2 = time.time()
print("정해준 n값 = %d, 결과값 = %d, time = %.6f" %(n, fibo(n), time.time()-start2))
"""
