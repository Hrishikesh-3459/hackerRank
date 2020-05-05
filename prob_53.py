def kaprekarNumbers(p, q):
    flag = False
    for i in range(p,q+1):
        if (i == 1 or i == 9):
            print(i, " " , end = "")
        width = len(str(i))
        num = str(i * i)
        tot = 0
        if (width != 1):
            tot = int(num[ : len(num)-width]) + int(num[len(num)-width : ])
        if (tot == i ):
            print(i, " " , end = "")
            flag = True
        tot = 0
    if(flag == False):
        print("INVALID RANGE")

kaprekarNumbers(1,10000)
