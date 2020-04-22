def birthday(s, d, m):
    pieces = []
    count = 0
    for i in range(len(s)):
        pieces = s[i:(m+i)]
        if(sum(pieces) == d):
            count += 1

    print(count)

birthday([1,2,1,3,2], 3, 2)