def breakingRecords(scores):
    min_score = scores[0]
    max_score = scores[0]
    count = [0,0]
    for i in range(1,len(scores)):
        if(scores[i] < min_score):
            min_score = scores[i]
            count[1] += 1
        elif(scores[i] > max_score):
            max_score = scores[i]
            count[0] += 1
    return(count)

    