def plusMinus(arr):
    total = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if(i>0):
            positive += 1
        elif(i<0):
            negative += 1
        else:
            zero += 1
    print(positive/total)
    print(negative/total)
    print(zero/total)

plusMinus([-4,3,-9,0,4,1])