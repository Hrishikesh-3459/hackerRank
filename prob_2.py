def compareTriplets(a, b):
    score = [0,0]
    for i in range(len(a)):
        if(a[i] > b[i]):
            score[0] += 1
        if(a[i] < b[i]):
            score[1] += 1
    return(score)

print(compareTriplets([17,28,30], [99,16,8]))