while True :
    try :
        n = int(input("Enter Number : "))
    except :
        print("Wrong Number")
    else :
        if n == -1 :
            print("Program shut down")
            break
        elif n < -1 :
            print("Wrong Number")
        else :
            i = 1
            a = 1
            while i <= n :
                a = a * i
                i = i + 1
            print(a)