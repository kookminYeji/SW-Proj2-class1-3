def factorial(n) :
    if n == 1 or n == 0:
        return 1
    else :
        return n * factorial(n-1)

while True :
    n = int(input("Enter a number : "))
    a = factorial(n)
    print(n, "!=", a)