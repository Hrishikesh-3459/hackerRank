def getTotalX(a, b):    
    ans = 0
    for i in range(1,min(b)+1):
        f1 = 0
        f2 = 0
        for j in a:
            if (i%j != 0):
                f1 += 1
        for k in b:
            if (k%i != 0):
                f2 += 1
        if (f1 == 0 and f2 == 0):
            ans += 1

    return(ans)

getTotalX([3,4], [24,48])
