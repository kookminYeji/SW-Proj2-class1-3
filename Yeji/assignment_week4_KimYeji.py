# 팩토리얼을 재귀함수로
def factorial(n):
   if (n <= 1):
      return 1

   return factorial(n-1) * n

# # 조합을 재귀함수로 나타낸 팩토리얼로 짜기
# if __name__ == '__main__':
#    n = int(input("num1 : "))
#    r = int(input("num2 : "))
#
#
#    result = factorial(n) / (factorial(r) * factorial(n-r))
#
#    print(result)


# 조합을 재귀함수로(파스칼)
def com(n,r):
    if (n==r or r==0):
        return  1
    else:
        return  com(n-1,r-1)+com(n-1,r)

print ("nCr")
n = int(input("n : "))
r = int(input("r : "))
print( com(n,r))






