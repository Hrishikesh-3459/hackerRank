def countingValleys(n, s):
    items = []
    valley = 0
    sea_level = 0
    for i in s:
        # print(sea_level)
        if(i == 'U'):
            sea_level +=1
            items.append(sea_level)
        else:
            sea_level -= 1
            items.append(sea_level)
        # if(sea_level == 0):
        #     valley += 1
    for i in range(len(items)):
        if(items[i] == 0 and items[i-1] < 0):
            valley += 1
    # print(items)
    return(valley)


print(countingValleys(8, "UDDDUDUU"))