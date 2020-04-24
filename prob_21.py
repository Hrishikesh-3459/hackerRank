def pageCount(n, p):
    front_count = -1
    if(n%2 == 0):
        back_count = 0
    else:
        back_count = -1
    for i in range(1,n,2):
        front_count += 1
        if(i == p or (i-1) == p):
            break
    for j in range(n,1,-2):
        back_count += 1
        if(j == p or (j-1) == p):
            break
    print("front: ", front_count)
    print("back: ", back_count)
    return(min(front_count, back_count))


pageCount(6,4)