import math


def viralAdvertising(n):
    shared = 5
    cumu = 0
    for i in range(n):
        liked = math.floor(shared / 2)
        shared = liked * 3
        cumu += liked 

    return(cumu)


print(viralAdvertising(4))


# 2 5 9 15 24