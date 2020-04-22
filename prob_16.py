def divisibleSumPairs(n, k, ar):
    # pairs = 0
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if((ar[i] + ar[j]) % k == 0):
                count += 1


    print(count)

divisibleSumPairs(6, 3, [1,3,2,6,1,2])


