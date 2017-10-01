num = int(input())
knum = int(input())

def factorialRecursive(n):
    return 1 if n == 1 else n * factorialRecursive(n-1)

def factorial_wf(n):
    i = 0
    _factorial = 1
    while i < n:
        _factorial = _factorial * ( i + 1)
        i+=1
    return _factorial


def Combination(n,k):
    if k == 0 or n == k:
        return 1
    elif n < k:
        print(" n < k cannot do it")
    else:
        return int(Combination(n-1,k-1)+Combination(n-1,k))

def Combination_wf(n,k):
    return int(factorial_wf(n) / (factorial_wf(k) * factorial_wf(n-k)))


print(factorialRecursive(num))
print(factorial_wf(num))

print(Combination_wf(num,knum))
print(Combination(num,knum))




