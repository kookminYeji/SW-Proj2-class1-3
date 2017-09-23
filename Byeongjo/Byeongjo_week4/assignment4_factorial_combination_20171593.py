def factorial(n) :
    if n == 1 or n == 0:
        return 1
    else :
        return n * factorial(n-1)


n = int(input("Enter n : "))
m = int(input("Enter m : "))

c = factorial(n)
d = factorial(m)
e = factorial(n-m)
print("C(",n,",",m,")" + "=", int(c/(d*e)))