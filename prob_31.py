def beautifulDays(i, j, k):
    days = list(range(i,j+1))
    count = 0
    for i in days:
        rev = (str(i))[::-1]
        numb = i - int(rev)
        if(numb % k == 0):
            count += 1

    return(count)


print(beautifulDays(20,23,6)  )