def factorial(n) :
    if n == 1 or n == 0 or n == -1:
        return 1
    else :
        return n * factorial(n-1)


n = int(input("Enter n : "))
m = int(input("Enter m : "))

c = factorial(n-1)
d = factorial(m)
e = factorial((n-1)-m)
f = int(c/(d*e))
d = factorial(m-1)
e = factorial((n-1)-(m-1))
g = int(c/(d*e))
print("C(",n,",",m,")" + "=", f+g)
