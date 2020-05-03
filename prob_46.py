def circularArrayRotation(a, k, queries):
    ans = []
    for i in range(k):
        aage = a[0:len(a)-1]
        last = a[-1]
        a.clear()
        a.append(last)
        a.extend(aage)
    for i in queries:
        ans.append(a[i])

    return(ans)


print(circularArrayRotation([1,2,3], 2, [0,1,2]))