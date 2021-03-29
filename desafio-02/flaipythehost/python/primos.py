for n in range(10000):
    if (n>=2):
        if (n==2 or n==3 or n==5 or n==7):
            print(n)
        elif (n % 2 != 0):
            if (n % 3 != 0):
                if (n % 5 !=0):
                    if (n % 7 != 0):
                        print(n)
