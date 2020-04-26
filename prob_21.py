def pageCount(n, p):
    if(p == 1):
        return(0)
    if((n%2 == 1) and (p == n or p == (n-1))):
        return(0)
    if((n%2 == 0) and (p == n)):
        return(0)
    front_count = 0
    back_count = 0
    for i in range(2,n,2): # To count from front
        front_count += 1
        if(i == p or (i+1) == p):
            break
    if(n%2 == 0):
        for i in range(n-1, 0, -2):
            back_count += 1
            if(i == p or (i-1) == p):
                break
    if(n%2 == 1):
        for i in range(n-2, 0, -2):
            back_count += 1
            if(i == p or (i-1) == p):
                break
    # print("front: ", front_count)
    # print("back: ", back_count)
    return(min(front_count, back_count))
pageCount(6,4)

#The code above is working perfectly but it isn't very efficient

# return(min(p/2, (n/2 - p/2))
# This is the ideal solution provied in the comments