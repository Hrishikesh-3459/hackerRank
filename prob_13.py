def getTotalX(a, b):    
    ans = 0
    factors=[]
    for num in b:
        for i in range(1,num+1):
            if num%i==0:
                factors.append(i)
    factors.remove(1)
    com = set(factors)
    for i in com:
        for j in a:
            if(i % j != 0):
                break
            else:
                ans += 1
            
    print(ans)

getTotalX([3,4], [24,48])
