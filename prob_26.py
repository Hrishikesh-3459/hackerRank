def pickingNumbers(a):
    plus_one = []
    minus_one = []
    max_len = []
    for i in range(len(a)):
        for j in a:
            if (j == a[i] or j == a[i]+1):
                plus_one.append(j)
            elif (j == a[i] or j == a[i]-1):
                minus_one.append(j)
        if (len(plus_one) > len(minus_one)):
            max_len.append(len(plus_one))
        else:
            max_len.append(len(minus_one))
        plus_one.clear()
        minus_one.clear()
    return(max(max_len))

    


print(pickingNumbers([1,2,2,3,1,2]))

