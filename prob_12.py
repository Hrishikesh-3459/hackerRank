def kangaroo(x1, v1, x2, v2):
    for i in range(100000):
        if(x1 == x2):
            return("yes")
        x1 += v1
        x2 += v2
    return("No")


print(kangaroo(0,2,5,3))