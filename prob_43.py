def extraLongFactorials(n):
    ans = 1
    for i in range(n,1,-1):
        ans *= i

    print(ans)