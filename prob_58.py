def beautifulTriplets(d, arr):
    counter = 0
    for i in arr:
        if ((i + d) in arr and (i + d + d) in arr):
            counter += 1

    return(counter)
