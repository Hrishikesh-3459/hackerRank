def countApplesAndOranges(s, t, a, b, apples, oranges):
    house = []
    apples_in_house = 0
    oranges_in_house = 0
    for i in range(s,t+1):
        house.append(i)
    for i in range(len(apples)):
        apples[i] += a
    for i in range(len(oranges)):
        oranges[i] += b
    for i in apples:
        if(i in house):
            apples_in_house += 1
    for i in oranges:
        if(i in house):
            oranges_in_house += 1
    print(apples_in_house)
    print(oranges_in_house)

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
