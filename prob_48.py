def equalizeArray(arr):
    freq = max(set(arr), key = arr.count)
    return(len(arr) - arr.count(freq))

print(equalizeArray([]))