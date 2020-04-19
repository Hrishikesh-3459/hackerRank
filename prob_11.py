def countApplesAndOranges(s, t, a, b, apples, oranges):
    li_ap = []
    li_or = []
    for x in apples:
        if((x+a) >= s and (x+a) <= t):
            li_ap.append(1)
    for j in oranges:
        if((j+b) >= s and (j+b) <= t):
            li_or.append(1)
    print(sum(li_ap))
    print(sum(li_or))

countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4])
