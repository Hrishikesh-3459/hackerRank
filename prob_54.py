def serviceLane(n, cases):
    width = [] # Given in the question
    ans = []
    for i in cases:
        ans.append(min(width[i[0]:i[1]+1]))

    return(ans)
    