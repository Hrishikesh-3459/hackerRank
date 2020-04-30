def findDigits(n):
    counter = 0
    for i in str(n):
        if(int(i) == 0):
            continue
        if(n % int(i) == 0):
            counter += 1

    return(counter)