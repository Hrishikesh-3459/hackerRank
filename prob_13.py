def getTotalX(a, b):    
    test1 = False
    test2 = False
    ans = 0
    i = 1
    while(i<1000):
        for j in a:
            if(j % i == 0):
                test1 = True
        for j in b:
            if(j % i == 0):
                test2 = True 
        if((test1 == True) and (test2 == True)):
            ans += 1
            test1 = False
            test2 = False
        i += 1
    print(ans)

getTotalX([3,4], [24,48])
