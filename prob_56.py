def chocolateFeast(n, c, m):
    bars = int(n / c)
    wrappers = bars

    while (wrappers >= m):
        wrappers -= m
        bars += 1
        wrappers += 1
    
    return(bars)




print(chocolateFeast(12,4,4))