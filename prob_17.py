def migratoryBirds(arr):
    max_count = 0
    ans = 0
    for i in arr:
        temp_count = arr.count(i)
        if(temp_count > max_count):
            max_count = temp_count
            ans = i
        elif((temp_count == max_count) and (ans > i)):
            ans = i
    return(ans)

print(migratoryBirds([2,2,1,1]))

