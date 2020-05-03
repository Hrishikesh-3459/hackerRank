import math

def squares(a, b):
    square = []
    for i in range(b):
        square.append(i*i)
    out = 0
    for i in range(a,b+1):
        if(math.sqrt(i) in square):
            out += 1

    return(out)


print(squares(35,70))