def jumpingOnClouds(c, k):
    n = len(c)
    health = 100
    if (c[0] == 1):
        health -= 2
    i = 0
    while True:
        health -= 1
        if (c[(i + k) % n] == 1):
            health -= 2
        i += 1
        if(c.index(c[(i + k) % n]) == 0):
            break

        
        

    # for i in range(0,n,k):
    #     health -= 1
    #     if (c[(i + k) % n] == 1):
    #         health -= 2
    return(health)


print(jumpingOnClouds([1,1,1,0,1,1,0,0,0,0], 3))

