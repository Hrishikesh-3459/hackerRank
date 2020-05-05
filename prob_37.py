def jumpingOnClouds(c, k):
    n = len(c)
    energy = 100
    if (k < len(c)):
        if (c[k] == 1):
            energy -= 3
        elif (c[k] == 0):
            energy -= 1
    i = k
    while (i != 0):
        i = (i+k) % n
        if (c[i] == 1):
            energy -= 3
        elif (c[i] == 0):
            energy -= 1
    return(energy)

        



print(jumpingOnClouds([1,1,1,0,1,1,0,0,0,0], 3))

